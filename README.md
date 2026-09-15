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

The page ships with **no data source at all**, because this repository is public and anything named
here points the whole internet at that data. There are three ways to feed it, in order of how
much they expose:

| Setting | What is exposed | Freshness |
| --- | --- | --- |
| `csvUrl` — a published anonymised tab | only that tab | a few minutes behind |
| `sheetId` — a sheet shared "Anyone with the link" | the whole spreadsheet | instant |
| `?sheet=<id>` in the address | nothing in the repo; only whoever holds the link | instant |

Use **`csvUrl` for the students' page** and **`?sheet=` for the copy you project**. The recipe is
below.

Columns are found by name, so you can reorder them. The page looks for headings containing:
*timestamp / 時間戳記*, *keyword*, *drive link*, *AI tools*, *AI-generated summary*,
*your own summary*, *agree*, *verify*. Name, student number and email columns are never read.

If Google is ever unreachable in class: **File → Download → CSV**, then **Paste CSV instead** on
the page.

## Sharing it with students

**It costs nothing to run.** No AI calls, no API keys, no accounts — nothing students do is billed
to anyone. The page's only automatic requests are `content/*.md`, the CSV, and Google Fonts.
Everything else on it is an ordinary link that opens in their own browser.

**The page shows no identities.** There is no "show names" control and no link to the sheet, and it
does not even read the name, student-number or email columns. Answers appear as *Student 01,
Student 02…*, numbered by submission time, so one person keeps one label all session. To put a name
to *Student 07*, open the response sheet yourself.

### Giving students live answers safely

The spreadsheet itself never needs to be public. Publish one anonymised **tab** instead:

1. In the response spreadsheet, add a tab and call it **Class view**.
2. In its cell A1:

   ```
   =QUERY('表單回應 1'!A:M, "select A, G, I, J, K, L, M", 1)
   ```

   Replace `表單回應 1` with the responses tab's real name — read it off the bottom of the window;
   Sheets autocompletes once you type `='`. That keeps timestamp, keyword, tools, both summaries,
   the agree answer and the verify answer. It drops names, student numbers, both email columns, and
   the Drive links (a shared Drive folder can show its owner's name).
3. **File → Share → Publish to web**. Choose **Class view**, not the whole document, and
   **Comma-separated values (.csv)**. Publish, and copy the link.
4. Put that link in `index.html` and push:

   ```js
   csvUrl: "https://docs.google.com/spreadsheets/d/e/2PACX-…/pub?gid=…&single=true&output=csv",
   ```

5. Now close the spreadsheet itself: **File → Share → General access → Restricted**. Publishing to
   web is independent of sharing, so the CSV keeps working while nobody can open the file. Reload
   the student page once to confirm answers still appear.

One trade-off: a published CSV can lag a few minutes behind a new submission. That is fine in
practice — project your own `?sheet=` link, which is instant, and the students' page catches up.

If you would rather not show live answers at all, leave both settings empty. Steps 2–5 work fully
on their own, and Step 1 says the answers are looked at together in the seminar.

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
