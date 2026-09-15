#!/usr/bin/env python3
"""Builds one self-contained HTML file with the content/*.md files inlined.

    python3 build-single-file.py

Writes seminar-standalone.html next to this script. Use it when you need to hand
over or upload a single file (an LMS page, an email attachment). Editing stays in
content/*.md — re-run this after every edit.

The standalone file still needs to be opened over http(s) for the Google Sheet to
load; that is Google's rule, not this page's.
"""
import pathlib, re, sys

here = pathlib.Path(__file__).resolve().parent
html = (here / "index.html").read_text(encoding="utf-8")
files = {
    "1": "content/01-answers.md",
    "2": "content/02-keywords.md",
    "3": "content/03-compare.md",
    "4": "content/04-verify.md",
    "5": "content/05-tools.md",
}

blocks = []
for key, rel in files.items():
    path = here / rel
    if not path.exists():
        sys.exit(f"missing {rel}")
    text = path.read_text(encoding="utf-8").replace("</script", "<\\/script")
    blocks.append(f'<script type="text/markdown" id="md{key}">\n{text}\n</script>')

if 'id="md1"' in html:
    sys.exit("index.html already contains inlined markdown — build from a clean copy")

anchor = "<body>"          # the blocks must sit before the script that reads them
if anchor not in html:
    sys.exit("could not find <body> in index.html — was it edited?")
out = html.replace(anchor, anchor + "\n" + "\n".join(blocks), 1)
target = here / "seminar-standalone.html"
target.write_text(out, encoding="utf-8")
kb = target.stat().st_size / 1024
print(f"wrote {target.name} ({kb:.0f} KB) with {len(blocks)} sections inlined")
