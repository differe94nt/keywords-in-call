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
if len(sys.argv) > 1:                 # e.g. python3 build-single-file.py 0923
    here = (here / sys.argv[1]).resolve()
html = (here / "index.html").read_text(encoding="utf-8")
# content/<nn>-name.md  ->  script id "md<nn>";  content/refs.md -> "mdr"
def key_for(name):
    m = re.match(r"^0*(\d+)[-_]", name)
    return m.group(1) if m else name[0]

sources = sorted((here / "content").glob("*.md"))
if not sources:
    sys.exit(f"no markdown found in {here / 'content'}")
files = {key_for(p.name): p.relative_to(here).as_posix() for p in sources}

blocks = []
for key, rel in sorted(files.items()):
    path = here / rel
    text = path.read_text(encoding="utf-8").replace("</script", "<\\/script")
    blocks.append(f'<script type="text/markdown" id="md{key}">\n{text}\n</script>')

if 'id="md1"' in html:
    sys.exit("index.html already contains inlined markdown — build from a clean copy")

anchor = "<body>"          # the blocks must sit before the script that reads them
if anchor not in html:
    sys.exit("could not find <body> in index.html — was it edited?")
out = html.replace(anchor, anchor + "\n" + "\n".join(blocks), 1)
target = here / (here.name + "-standalone.html" if here.name != "seminar" else "seminar-standalone.html")
target.write_text(out, encoding="utf-8")
kb = target.stat().st_size / 1024
print(f"wrote {target.name} ({kb:.0f} KB) with {len(blocks)} sections inlined")
