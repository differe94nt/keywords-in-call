# Seminar page — how to run and edit it

```
seminar/
  index.html              the page (settings at the top, nothing else to touch)
  content/
    01-answers.md         Step 1 text + the discussion prompts
    02-keywords.md        Step 2 — one block per keyword card
    03-compare.md         Step 3 — the comparison topics
    04-verify.md          Step 4 — the seven checks + red flags
    05-tools.md           Step 5 — the AI tools
  serve.command           double-click to preview on this Mac
  build-single-file.py    optional: squash everything into one .html
  seminar-standalone.html the result of that (regenerate after edits)
```

Publish the **folder** normally. Use the standalone file only where a folder is awkward —
an LMS page, an email attachment. Rebuild it after editing any `.md`:

```
python3 build-single-file.py
```

## Preview it on your own machine

Double-click `serve.command`, or in Terminal:

```
cd path/to/seminar
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

**Opening `index.html` by double-clicking will not work.** Browsers block a page loaded from
disk (`file://`) from reading the `content/*.md` files and from reading Google Sheets. It has to
be served over `http://` — locally, or on a host.

## Publish it for students

Any static host works. GitHub Pages, in four steps:

1. Put these files in a GitHub repository.
2. Repo **Settings → Pages → Source: Deploy from a branch**, branch `main`, folder `/` (or `/docs`).
3. Wait a minute; the page appears at `https://<you>.github.io/<repo>/`.
4. Give students that link.

Alternatives that need no GitHub: Netlify Drop (drag the folder onto <https://app.netlify.com/drop>),
Cloudflare Pages, or your university web space.

## The response sheet

The page reads the sheet live through Google's CSV endpoint. The sheet must be shared
**Anyone with the link → Viewer**, and the page needs its ID — the part of the sheet URL between
`/d/` and `/edit`.

`sheetId` ships **empty**, because this file is public and an ID in it makes that sheet findable by
anyone. Fill it one of two ways:

- **For everyone, permanently:** put an *anonymised* sheet's ID in `index.html` (recipe below).
- **For one visit:** add it to the address instead, and commit nothing —

  ```
  https://<your-pages-url>/?sheet=<the response sheet’s id>
  ```

  Keep that link to yourself: it is the real response sheet. Add `&gid=<gid>` for a specific tab.

Columns are found by name, so you can reorder them in the sheet. The page looks for headings
containing: *timestamp / 時間戳記*, *keyword*, *drive link*, *AI tools*, *AI-generated summary*,
*your own summary*, *agree*, *verify*. The name, student-number and email columns are never read —
see below.

If Google is ever unreachable in class: **File → Download → CSV** in Sheets, then use
**Paste CSV instead** on the page.

## Sharing it with students

**It costs nothing to run.** The page has no AI calls, no API keys and no accounts, so nothing
students do is billed to anyone. Its only automatic requests are the `content/*.md` files, the
sheet's CSV, and Google Fonts. Every other site on it (Scholar, Crossref, ChatGPT…) is an ordinary
link that opens in the student's own browser under their own account.

**The page shows no identities at all.** There is no "show names" control and no link to the sheet.
It does not even read the name, student-number or email columns — it maps only timestamp, keyword,
tools, the two summaries, the agree answer and the verify answer. Answers appear as
*Student 01, Student 02…*, numbered by submission time, so the same person keeps the same label all
session. To put a name to *Student 07*, open the response sheet yourself.

**The sheet is still the thing to protect.** Any sheet this page reads has to be readable by
anyone with the link, so whoever learns its ID can open it and read every column, emails included.
Hiding a tab does not help — Google shares whole files, not tabs. That is why `sheetId` ships empty
and why the `?sheet=` link above is yours alone.

To give students live answers safely, publish a **separate, anonymised spreadsheet** and put *that*
ID in the file:

1. New spreadsheet, e.g. *Seminar — class view*. A **separate file**, not a new tab.
2. In cell A1:

   ```
   =QUERY(IMPORTRANGE("<paste the response sheet's URL>","表單回應 1!A:M"),
          "select Col1, Col7, Col9, Col10, Col11, Col12, Col13", 1)
   ```

   Replace `表單回應 1` with your responses tab's real name (bottom-left of the sheet). This keeps
   timestamp, keyword, tools, both summaries, the agree answer and the verify answer, and drops
   names, student numbers, both emails and the Drive links. Click **Allow access** when prompted.
3. Share *that* file: **Anyone with the link → Viewer**. Leave the response sheet private.
4. Put its ID in `index.html`:

   ```js
   sheetId: "<the class-view sheet's id>",
   ```

Then the published page is anonymous all the way down, not just on screen.

If you would rather not publish live answers at all, set `sheetId: ""`. Steps 2–5 work fully on
their own, and Step 1 says the answers are looked at together in the seminar.

## Editing the content

Each `.md` file is ordinary Markdown with a few labelled lines. A `##` heading starts a new item
(a keyword card, a topic, a check, a tool); the `label: value` lines under it fill the parts of that
item. Each file carries a comment at the top listing the labels it accepts.

To add an eleventh keyword, copy an existing block in `02-keywords.md` and edit it — the coverage
grid, the comparison table, the filters and the card grid all pick it up automatically.

`match:` is the line that connects a card to the form answers. Put in it whatever students might
type or select, separated by `|`.

Citations: add `| doi:10.1016/S0346-251X(02)00071-4` after a source to give it a direct DOI button.
Without one, it still gets Scholar / Crossref / OpenAlex / Semantic Scholar lookups.

## One caution about the reference lists

The citations in `02-keywords.md` are starting points typed from memory, and a wrong year or
journal is entirely possible. That is deliberate — students verify them through the buttons, which
is the point of Step 4 — but do not reuse them in a syllabus or handout without checking them first.
