#!/usr/bin/env python3
"""Append a note line to a section of exclusions.md:  python3 note.py SECTION "text" ["text" ...]"""
import sys, os
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exclusions.md")
section, lines = sys.argv[1].upper(), sys.argv[2:]
text = open(path, encoding="utf-8").read().split("\n")
hdr = f"## {section}"
if hdr not in text:
    raise SystemExit(f"no section {hdr}")
i = text.index(hdr) + 1
while i < len(text) and not text[i].startswith("## "):
    i += 1
# insert before trailing blank line of the section
j = i
while j > 0 and text[j - 1].strip() == "":
    j -= 1
for k, ln in enumerate(lines):
    text.insert(j + k, "- " + ln)
open(path, "w", encoding="utf-8").write("\n".join(text))
