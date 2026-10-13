#!/usr/bin/env python3
"""Generate coverage_report.md from deck_build/coverage.json (written by build.py),
exclusions.md and excluded_los.txt.  Run build.py first:  python3 deck_build/report.py"""
import json
import os
import re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "coverage_report.md")

cov = json.load(open(os.path.join(HERE, "coverage.json"), encoding="utf-8"))
sections, items = cov["sections"], cov["items"]


def ranges(pages):
    pages = sorted(set(pages))
    out, start, prev = [], None, None
    for p in pages:
        if start is None:
            start = prev = p
        elif p == prev + 1:
            prev = p
        else:
            out.append(f"{start}" if start == prev else f"{start}-{prev}")
            start = prev = p
    if start is not None:
        out.append(f"{start}" if start == prev else f"{start}-{prev}")
    return ", ".join(out)


def read_notes():
    notes, cur = defaultdict(list), None
    for line in open(os.path.join(HERE, "exclusions.md"), encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("## "):
            cur = line[3:].strip()
        elif line.startswith("- ") and cur:
            notes[cur].append(line[2:].strip())
    return notes


def page_key(note):
    m = re.match(r"p(\d+)", note)
    return int(m.group(1)) if m else 0


def read_excluded_los():
    by_sec = defaultdict(list)
    for line in open(os.path.join(HERE, "excluded_los.txt"), encoding="utf-8"):
        if not line.strip() or line.startswith("#"):
            continue
        sec, lo, pages = [x.strip() for x in line.split("|")]
        by_sec[sec].append((lo, pages))
    return by_sec


def md_escape(s):
    return s.replace("|", "\\|")


def strip_html(s):
    s = re.sub(r"<br>", " ", s)
    return re.sub(r"<[^>]+>", "", s).replace("&amp;", "&")


notes = read_notes()
excl = read_excluded_los()
total = cov["total"]
n_items = len(items)
n_verify = len(cov["verify_cards"])
type_counts = cov["type_counts"]

L = []
w = L.append
w("# Coverage report: microeconomics Anki deck")
w("")
w(f"**Deck file:** `econ_u4_qcaa.csv` | **Cards:** {total} | **Checklist items:** {n_items} "
  f"(all have at least 2 cards) | **Calculation cards:** 0 | **`verify` cards:** {n_verify}")
w("")
w("**Source:** *Economics for the IB Diploma* (Tragakes, 3rd ed., Cambridge 2020), the trimmed PDF in this repo: "
  "Chapters 2-7, book pages 41-245 (PDF page = book page - 40). All page numbers below are **book** page numbers, "
  "so you can find them in the printed book or in the PDF's page footers.")
w("")
w("## Calls I made")
w("")
calls = [
    "**Scope.** You asked for everything in the PDF except Theory of Knowledge (TOK) boxes and calculations. "
    "The PDF is the whole IB microeconomics unit (Chapters 2-7, SL and HL), so every section is carded, "
    "including HL-only sections (behavioural economics, asymmetric information, equity, all of Chapter 7).",
    "**No calculation cards.** The validation rule 'no formula or worked-number cards' wins over the template's "
    "formula/worked-example instructions. So the deck has no MathJax, no formula cards and no worked examples. "
    "Formula-only ideas are carded in words where they carry meaning (e.g. 'average revenue is revenue per unit, "
    "so it equals price'). Every excluded calculation is listed below.",
    "**Checklist.** No QCAA checklist came with the request, so the checklist is the textbook's own learning "
    "objectives for each section. Where one objective covers several sub-topics (e.g. 'explain the consequences "
    "of price controls'), I split it along the book's own sub-headings. Dot-point tags follow the book's numbering: "
    "`T4.2.6` = section 4.2, item 6. The generic 'define all the terms' objective is folded into the item each term "
    "belongs to. Because the checklist comes from the book, every item has textbook coverage; no item is 'not in textbook'.",
    "**Header and file name kept exactly as specified** (`#deck:Economics::Unit 4 EA`, `econ_u4_qcaa.csv`), even "
    "though the content is microeconomics. Rename the deck in Anki after import if you want (e.g. `Economics::Micro`).",
    "**Topic tags** are one per textbook section (e.g. `price_controls`, `monopoly`). **Type tags:** the requested "
    "`definition`, `chain`, `diagram`, `evaluation` and `verify`, plus four more so every card has a type: "
    "`distinguish` (X vs Y), `stakeholders` (effects on groups), `example` and `explain`. `calc` is never used.",
    "**Australian context.** The book is international, so I added "
    f"{n_verify} Australian application cards written from my own knowledge, all tagged `verify` (list below). "
    "They cover the ACCC and the Competition and Consumer Act, the Fair Work Commission, GST and excise, carbon "
    "pricing and the Safeguard Mechanism, Murray-Darling water trading, the PBS, Medicare, HECS-HELP, and similar. "
    "They are filed under the dot point they illustrate. Suspend the tag `verify` if you don't want them.",
    "**Real world focus boxes and examples** in the main text are carded as `example` cards, since EA answers need "
    "examples. 'Test your understanding', 'Applying your skills', 'Inquiry and reflection' and exam-style "
    "questions add no new content, so they are not carded (the concepts they test are).",
    "**Australian spelling and terminology** throughout (labour, behaviour, maximise, programs, aluminium, sulfur). "
    "Official names keep their own spelling (World Health Organization, OPEC). The validator checks for "
    "American spellings.",
    "**Text extraction.** The PDF has a text layer (pdftotext), so OCR wasn't needed to read it. But the orange "
    "key terms on some Chapter 7 pages (e.g. 'market power', 'economies of scale', 'normal profit') were missing "
    "from that layer. I OCR'd every page with tesseract (colour-to-black preprocessing) and diffed it against the "
    "text layer to recover them. Chapters 2-6 had no missing content.",
    "**Textbook errors corrected** in the cards (listed at the end) rather than copied.",
]
for c in calls:
    w(f"- {c}")
w("")

# ---------------- checklist table ----------------
w("## Checklist coverage")
w("")
w("Each row is one checklist item (a textbook learning objective) with its card count and the textbook pages the "
  "cards come from. *AU* means the item also has Australian-context `verify` cards written from my own knowledge. "
  "Calculation-only objectives appear as struck-out rows with 0 cards.")
w("")
for sec, meta in sections.items():
    sec_items = [(iid, d) for iid, d in items.items() if d["section"] == sec]
    sec_total = sum(d["count"] for _, d in sec_items)
    w(f"### {sec} {meta['title']} (tag `{meta['topic']}`, {sec_total} cards)")
    w("")
    w("| Dot point | Checklist item | Cards | Textbook pages |")
    w("|---|---|---:|---|")
    for iid, d in sec_items:
        pages = ranges(d["pages"]) if d["pages"] else "not in textbook"
        if d["own_knowledge"]:
            pages += " + AU"
        w(f"| `{iid}` | {md_escape(d['desc'])} | {d['count']} | {pages} |")
    for lo, pages in excl.get(sec, []):
        w(f"| - | ~~{md_escape(lo)}~~ (excluded: calculation) | 0 | {pages} |")
    w("")

# ---------------- counts ----------------
w("## Card counts")
w("")
w("| Topic tag | Cards |")
w("|---|---:|")
for sec, meta in sections.items():
    w(f"| `{meta['topic']}` | {cov['topic_counts'].get(meta['topic'], 0)} |")
w(f"| **Total** | **{total}** |")
w("")
w("| Type tag | Cards |")
w("|---|---:|")
for t in sorted(type_counts, key=lambda k: -type_counts[k]):
    w(f"| `{t}` | {type_counts[t]} |")
w(f"| `calc` | {type_counts.get('calc', 0)} |")
w("")
w("A card can carry more than one type tag, so the type counts add up to more than the total.")
w("")

# ---------------- verify ----------------
w(f"## `verify` cards ({n_verify})")
w("")
w("Australian-specific content written from my own knowledge (not in the IB textbook). Check each against "
  "current official sources (Fair Work Commission, ATO, ACCC, AER, DCCEEW/Clean Energy Regulator, MDBA, "
  "Department of Health, Treasury). Rules and figures change, e.g. merger law changed on 1 January 2026.")
w("")
w("| Dot point | Front |")
w("|---|---|")
for v in cov["verify_cards"]:
    w(f"| `{v['id']}` | {md_escape(strip_html(v['front']))} |")
w("")

# ---------------- exclusions ----------------
w("## IB calculations excluded")
w("")
w("Excluded on your instruction (no calculation cards). Conceptual points from these pages, such as what a "
  "surplus area represents or what MR = MC means, are still carded.")
w("")
for n in sorted(notes.get("CALCULATIONS", []), key=page_key):
    w(f"- {n}")
w("")
w("## Theory of knowledge boxes excluded")
w("")
w("Excluded on your instruction. Some contain evaluation points you might want (noted).")
w("")
for n in sorted(notes.get("TOK", []), key=page_key):
    w(f"- {n}")
w("")
w("## Borderline textbook content")
w("")
w("Content that is excluded, partly carded, or not actually in the PDF (the book points to its digital "
  "coursebook). Decide whether you want any of it added.")
w("")
for n in sorted(notes.get("BORDERLINE", []), key=page_key):
    w(f"- {n}")
w("")
w("## Textbook errors corrected in the cards")
w("")
for n in sorted(notes.get("CORRECTIONS", []), key=page_key):
    w(f"- {n}")
w("")
w("## Validation run before finishing")
w("")
checks = [
    "CSV re-parsed (skipping the six `#` header lines, which are written verbatim): every row has exactly 3 "
    "non-empty fields; row count matches the card sources.",
    "No duplicate fronts (compared case-insensitively, ignoring HTML and trailing punctuation). I also ran a "
    "near-duplicate similarity check by hand and removed 5 overlapping cards; the remaining similar pairs are "
    "deliberate mirrors (e.g. elastic vs inelastic, shift left vs right).",
    "HTML tags balanced, and only simple tags used (`<b>`, `<br>`). No markdown.",
    "MathJax delimiters balanced (none are used, as there are no calculation cards).",
    "No `calc` tags, and a pattern check for formulas or worked numbers (`Step 1`, `=` followed by a number, "
    "number-operator-number) finds none.",
    "Every checklist item has at least 2 cards; every card's dot-point tag exists in the checklist.",
    "Fronts don't refer to 'the text', 'this chapter', page, figure or table numbers.",
    "Spelling check for American spellings and IB-only terms.",
    "Every `verify` card is marked as own-knowledge (not attributed to textbook pages).",
]
for c in checks:
    w(f"- {c}")
w("")
w("## Rebuilding")
w("")
w("The deck is generated, not hand-edited. Card sources are in `deck_build/cards/*.txt`, the checklist is "
  "`deck_build/checklist.txt`, and exclusion notes are in `deck_build/exclusions.md`. "
  "Run `python3 deck_build/build.py` (writes and validates the CSV) and then `python3 deck_build/report.py` "
  "(writes this report).")
w("")

open(OUT, "w", encoding="utf-8").write("\n".join(L))
print(f"wrote {os.path.relpath(OUT, ROOT)} ({len(L)} lines)")
