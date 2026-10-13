#!/usr/bin/env python3
"""Build and validate the Anki deck econ_u4_qcaa.csv from the card sources.

Sources (all in this folder):
  checklist.txt  - checklist items (textbook learning objectives), grouped by section
  cards/*.txt    - card blocks:  @ <dot-point ID> | <type tags> | <book pages>
                                 Q: <front>
                                 A: <back>
                   Continuation lines are joined to the previous field with a space.
                   Lines starting with '#' are comments.

Run:  python3 deck_build/build.py
Writes econ_u4_qcaa.csv (repo root) and deck_build/coverage.json, prints counts,
and exits non-zero if any validation check fails.
"""
import csv
import glob
import html
import io
import json
import os
import re
import sys
from collections import Counter, OrderedDict, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CSV_PATH = os.path.join(ROOT, "econ_u4_qcaa.csv")
COVERAGE_PATH = os.path.join(HERE, "coverage.json")

HEADER_LINES = [
    "#separator:Comma",
    "#html:true",
    "#notetype:Basic",
    "#deck:Economics::Unit 4 EA",
    "#tags column:3",
    "#columns:Front,Back,Tags",
]

TYPE_TAGS = {
    "definition", "distinguish", "chain", "diagram", "stakeholders",
    "evaluation", "example", "explain", "verify",
}
# Calculations are out of scope for this deck, so "calc" is deliberately not allowed.

VOID_TAGS = {"br", "hr", "img"}
ALLOWED_HTML = {"b", "i", "u", "br", "ul", "ol", "li", "sub", "sup", "span", "div", "em", "strong"}

# Phrases that stop a front from standing alone.
FRONT_BANNED = [
    r"according to the text", r"\bthe text\b", r"in this chapter", r"this section",
    r"\bpage\b", r"\bp\.\s*\d", r"textbook", r"\bfigure\b", r"\btable\b",
    r"the book", r"the author",
]
ANY_BANNED = [r"\bfigure\s+\d", r"\btable\s+\d", r"\bin the text\b"]

# American spellings / IB terms that should be Australian / QCAA.
SPELLING = [
    r"\blabor", r"\bbehavior", r"utiliz", r"organiz", r"analyz", r"\bfavor", r"\bcolor",
    r"\bcenter", r"programme", r"maximiz", r"minimiz", r"subsidiz", r"realiz", r"recogniz",
    r"\bdefense\b", r"fulfill\b", r"enrollment", r"neighbor", r"\bgasoline\b", r"\bgas price",
    r"business cycle", r"criticiz", r"monopoliz", r"privatiz", r"optimiz", r"stabiliz",
    r"prioritiz", r"internaliz", r"specializ", r"emphasiz", r"categoriz", r"characteriz",
    r"rationaliz", r"standardiz", r"\bcatalog\b", r"\bjudgment", r"\btraveling", r"\bmodeling",
    r"\bfiber\b", r"\bmeter\b", r"\bliter\b", r"\bton\b", r"\btons\b", r"aluminum", r"\bsulphur",
]

# Proper nouns that keep their official (non-Australian) spelling.
PROPER_NOUNS = [r"World Health Organization", r"World Trade Organization", r"Organization of the Petroleum Exporting Countries"]

MARKDOWN = [r"\*\*", r"__", r"`", r"^\s*[-*] ", r"^\s*#", r"\[[^\]]+\]\([^)]+\)"]

# Heuristics for formula / worked-number content (calculations are excluded).
CALC_PATTERNS = [
    r"step\s*1", r"\\\(", r"\\\[", r"\d\s*[×x*÷/]\s*\d", r"\d\s*=\s*\d", r"=\s*\d",
    r"%\s*Δ", r"Δ\s*Q\s*/", r"\bworked example",
]


def fail(msg, errors):
    errors.append(msg)


def strip_html(s):
    return re.sub(r"<[^>]+>", "", s)


def norm_front(s):
    t = html.unescape(strip_html(s)).lower()
    t = re.sub(r"\s+", " ", t).strip()
    return re.sub(r"[\s?.!:]+$", "", t)


def html_balanced(s):
    """Return None if tags balance and every '<' starts an allowed tag, else a message."""
    stack = []
    pos = 0
    for m in re.finditer(r"<", s):
        tm = re.match(r"<(/?)([a-zA-Z]+)(\s[^<>]*)?\s*/?>", s[m.start():])
        if not tm:
            return f"stray '<' at col {m.start()}"
        closing, name = tm.group(1), tm.group(2).lower()
        if name not in ALLOWED_HTML:
            return f"tag <{name}> not allowed"
        if name in VOID_TAGS:
            continue
        if closing:
            if not stack or stack[-1] != name:
                return f"unbalanced </{name}>"
            stack.pop()
        else:
            stack.append(name)
    if stack:
        return f"unclosed <{stack[-1]}>"
    return None


def mathjax_balanced(s):
    for opener, closer in (("\\(", "\\)"), ("\\[", "\\]")):
        depth = 0
        i = 0
        while i < len(s):
            if s.startswith(opener, i):
                depth += 1
                if depth > 1:
                    return f"nested {opener}"
                i += 2
                continue
            if s.startswith(closer, i):
                depth -= 1
                if depth < 0:
                    return f"unmatched {closer}"
                i += 2
                continue
            i += 1
        if depth != 0:
            return f"unclosed {opener}"
    return None


def parse_checklist(path):
    sections = OrderedDict()   # num -> {topic, title}
    items = OrderedDict()      # id -> {desc, section, topic}
    current = None
    with open(path, encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            m = re.match(r"^\[(\S+)\s*\|\s*(\S+)\s*\|\s*(.+)\]$", line.strip())
            if m:
                current = m.group(1)
                sections[current] = {"topic": m.group(2), "title": m.group(3).strip()}
                continue
            m = re.match(r"^(T[\w.]+)\s*\|\s*(.+)$", line.strip())
            if not m or current is None:
                raise SystemExit(f"checklist.txt:{ln}: cannot parse: {line!r}")
            iid = m.group(1)
            if iid in items:
                raise SystemExit(f"checklist.txt:{ln}: duplicate item {iid}")
            items[iid] = {"desc": m.group(2).strip(), "section": current,
                          "topic": sections[current]["topic"]}
    return sections, items


def parse_cards(paths):
    cards = []
    for path in paths:
        name = os.path.basename(path)
        cur = None
        field = None
        with open(path, encoding="utf-8") as f:
            for ln, raw in enumerate(f, 1):
                line = raw.rstrip("\n")
                s = line.strip()
                if s.startswith("#"):
                    continue
                if s.startswith("@"):
                    if cur:
                        cards.append(cur)
                    parts = [p.strip() for p in s[1:].split("|")]
                    if len(parts) != 3:
                        raise SystemExit(f"{name}:{ln}: header needs 3 '|' fields: {s!r}")
                    types = [t for t in parts[1].split() if t != "-"]
                    cur = {"id": parts[0], "types": types, "pages": parts[2],
                           "q": "", "a": "", "src": f"{name}:{ln}"}
                    field = None
                    continue
                if not s:
                    field = None
                    continue
                if cur is None:
                    raise SystemExit(f"{name}:{ln}: text outside a card: {s!r}")
                if s.startswith("Q:"):
                    field = "q"
                    cur["q"] = s[2:].strip()
                elif s.startswith("A:"):
                    field = "a"
                    cur["a"] = s[2:].strip()
                elif field:
                    cur[field] = (cur[field] + " " + s).strip()
                else:
                    raise SystemExit(f"{name}:{ln}: continuation without Q:/A:: {s!r}")
        if cur:
            cards.append(cur)
    return cards


def page_list(pages):
    """'43-45, 47' -> [43, 44, 45, 47]; non-numeric tokens (e.g. 'AU') are kept as strings."""
    out = []
    for tok in re.split(r"[,\s]+", pages.strip()):
        if not tok:
            continue
        m = re.match(r"^(\d+)-(\d+)$", tok)
        if m:
            out.extend(range(int(m.group(1)), int(m.group(2)) + 1))
        elif tok.isdigit():
            out.append(int(tok))
        else:
            out.append(tok)
    return out


def main():
    errors, warnings = [], []
    sections, items = parse_checklist(os.path.join(HERE, "checklist.txt"))
    card_files = sorted(glob.glob(os.path.join(HERE, "cards", "*.txt")))
    cards = parse_cards(card_files)

    seen = {}
    for c in cards:
        where = c["src"]
        if c["id"] not in items:
            fail(f"{where}: unknown dot-point ID {c['id']}", errors)
            continue
        if not c["q"] or not c["a"]:
            fail(f"{where}: empty front or back", errors)
        bad = [t for t in c["types"] if t not in TYPE_TAGS]
        if bad:
            fail(f"{where}: unknown type tag(s) {bad}", errors)
        if "verify" in c["types"] and not any(str(p).upper() == "AU" for p in page_list(c["pages"])):
            fail(f"{where}: verify card must list AU (own knowledge) in pages", errors)
        if not c["pages"]:
            fail(f"{where}: no pages given", errors)
        key = norm_front(c["q"])
        if key in seen:
            fail(f"{where}: duplicate front (also {seen[key]}): {c['q']}", errors)
        seen[key] = where
        for label, text in (("front", c["q"]), ("back", c["a"])):
            msg = html_balanced(text)
            if msg:
                fail(f"{where}: {label} HTML: {msg}", errors)
            msg = mathjax_balanced(text)
            if msg:
                fail(f"{where}: {label} MathJax: {msg}", errors)
            for pat in MARKDOWN:
                if re.search(pat, text, re.M):
                    fail(f"{where}: {label} looks like markdown ({pat})", errors)
            plain = strip_html(text)
            for pn in PROPER_NOUNS:
                plain = re.sub(pn, "", plain)
            for pat in SPELLING:
                if re.search(pat, plain, re.I):
                    fail(f"{where}: {label} non-Australian spelling/term ({pat})", errors)
            for pat in ANY_BANNED:
                if re.search(pat, strip_html(text), re.I):
                    fail(f"{where}: {label} refers to the book ({pat})", errors)
            for pat in CALC_PATTERNS:
                if re.search(pat, strip_html(text), re.I):
                    fail(f"{where}: {label} looks like a formula/worked calculation ({pat})", errors)
        for pat in FRONT_BANNED:
            if re.search(pat, strip_html(c["q"]), re.I):
                fail(f"{where}: front does not stand alone ({pat})", errors)
        if len(strip_html(c["a"])) > 520:
            warnings.append(f"{where}: long back ({len(strip_html(c['a']))} chars)")

    per_item = Counter(c["id"] for c in cards)
    for iid in items:
        if per_item[iid] < 2:
            fail(f"checklist item {iid} has only {per_item[iid]} card(s)", errors)

    # ---- write CSV (header lines verbatim, rows via csv module) ----
    rows = []
    for c in cards:
        if c["id"] not in items:
            continue
        tags = [items[c["id"]]["topic"], c["id"]] + c["types"]
        rows.append([c["q"], c["a"], " ".join(tags)])
    with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
        for h in HEADER_LINES:
            f.write(h + "\n")
        w = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
        w.writerows(rows)

    # ---- re-parse CSV and validate ----
    with open(CSV_PATH, encoding="utf-8", newline="") as f:
        text = f.read()
    lines = text.split("\n")
    if lines[:len(HEADER_LINES)] != HEADER_LINES:
        fail("CSV header lines are not exactly as required", errors)
    body = "\n".join(lines[len(HEADER_LINES):])
    parsed = list(csv.reader(io.StringIO(body, newline="")))
    parsed = [r for r in parsed if r]
    fronts = Counter()
    for i, r in enumerate(parsed, 1):
        if len(r) != 3 or not all(x.strip() for x in r):
            fail(f"CSV row {i}: expected 3 non-empty fields, got {len(r)}", errors)
            continue
        fronts[norm_front(r[0])] += 1
        for x in r[:2]:
            if html_balanced(x):
                fail(f"CSV row {i}: HTML unbalanced", errors)
            if mathjax_balanced(x):
                fail(f"CSV row {i}: MathJax unbalanced", errors)
        if "calc" in r[2].split():
            fail(f"CSV row {i}: calc card present", errors)
    dups = [k for k, v in fronts.items() if v > 1]
    if dups:
        fail(f"CSV has {len(dups)} duplicate fronts", errors)
    if len(parsed) != len(rows):
        fail(f"CSV re-parse found {len(parsed)} rows, expected {len(rows)}", errors)

    # ---- counts ----
    topic_counts = Counter(r[2].split()[0] for r in parsed)
    type_counts = Counter(t for r in parsed for t in r[2].split()[2:])
    untyped = sum(1 for r in parsed if len(r[2].split()) == 2)
    print(f"Cards written: {len(parsed)}  ->  {os.path.relpath(CSV_PATH, ROOT)}")
    print("\nCards per topic tag:")
    order = [sections[s]["topic"] for s in sections]
    for t in order:
        print(f"  {t:28s} {topic_counts.get(t, 0):5d}")
    print("\nCards per type tag:")
    for t in sorted(type_counts, key=lambda k: -type_counts[k]):
        print(f"  {t:28s} {type_counts[t]:5d}")
    print(f"  {'(no type tag)':28s} {untyped:5d}")
    print(f"  {'calc':28s} {type_counts.get('calc', 0):5d}")

    # ---- coverage data for the report ----
    pages_by_item = defaultdict(set)
    for c in cards:
        for p in page_list(c["pages"]):
            pages_by_item[c["id"]].add(p)
    cov = {
        "sections": sections,
        "items": {iid: {**d, "count": per_item[iid],
                        "pages": sorted([p for p in pages_by_item[iid] if isinstance(p, int)]),
                        "own_knowledge": any(not isinstance(p, int) for p in pages_by_item[iid])}
                  for iid, d in items.items()},
        "verify_cards": [{"id": c["id"], "front": c["q"], "topic": items[c["id"]]["topic"]}
                         for c in cards if "verify" in c["types"] and c["id"] in items],
        "topic_counts": dict(topic_counts),
        "type_counts": dict(type_counts),
        "untyped": untyped,
        "total": len(parsed),
    }
    with open(COVERAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(cov, f, indent=1, ensure_ascii=False)

    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for w_ in warnings:
            print("  WARN", w_)
    if errors:
        print(f"\n{len(errors)} ERROR(S):")
        for e in errors:
            print("  ERR", e)
        sys.exit(1)
    print("\nAll validation checks passed.")


if __name__ == "__main__":
    main()
