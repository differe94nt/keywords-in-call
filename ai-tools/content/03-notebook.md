# Gemini Notebook for your literature review

Gemini Notebook (until recently called **NotebookLM**) answers questions **only from the sources you give it**, and links each claim to the passage it came from. That makes it good at one part of a literature review — reading across several papers quickly — and useless at another: deciding which papers are worth reading. You still choose the sources, read them, and write the review.

**Before the proposal deadline (11/04, 08:00):** aim for one notebook per project, five sources, a filled-in literature matrix, and a first idea of where your five sources agree and disagree. Week 8 (10/28) is preparation time — a good week to get this done.

<!--
HOW TO EDIT
  ## Title   kind: step (do / check / tip) · prompt (fenced ``` block) · card · section
-->

## Before you start
kind: card
- **Account:** open notebook.google.com with a Google account. If your university account does not show it, your school may have switched it off — use a personal account and do not upload anything confidential.
- **One notebook per project.** Name it with your working title.
- **Write your question first** — one sentence. Everything you ask the notebook will be measured against it.
- **Limits on the free plan:** 50 sources per notebook; each source up to 500,000 words or 200 MB.

## The workflow
kind: section

## Find candidate sources yourself first
kind: step
do: Search Google Scholar, ERIC or your library database with the keywords from Week 2. Save the PDFs of the most relevant studies. Prefer peer-reviewed journal articles and recent reviews.
tip: Inside the notebook, **Add sources** also has a search box: choose **Web** or **Drive** for a fast search, or use **Deep Research**, which browses many websites and compiles a report. Treat what it finds as *leads* — check that each one is a real, peer-reviewed study before you keep it.
check: Can you name the journal and year of every source? If not, it is not ready to cite.

## Create the notebook and add sources
kind: step
do: notebook.google.com → **Create new notebook** → **Add sources**. Upload the PDFs. Rename each source **Author (Year) short title** so citations are readable.
tip: Supported sources include PDF, Word, Google Docs and Slides, web pages, public YouTube videos with captions, audio files and pasted text. Google Drive files stay synced as you edit them.
check: Open each source in the left panel and make sure the full text loaded — not just a cover page or abstract.

## Read the core paper yourself
kind: step
do: Read the abstract, the research questions, the method and the conclusion of at least your most important source *before* asking the notebook about it.
check: You can only spot a wrong answer if you know roughly what the right one is.

## Set how the chat answers
kind: step
do: In the **Chat** panel select **Configure Chat**. Choose **Custom** and paste the role prompt below, or **Learning Guide** if you want it to explain methods step by step instead of answering directly. You can also set the response length.

## Extract one source at a time
kind: step
do: In the sources panel, tick **only one source**. Ask the extraction prompt. Repeat for each source.
check: Click each numbered citation — it jumps to the passage. Hover to see the quotation. Is the claim really in that passage?
tip: Select **Save to note** on a good answer. Saved notes keep their tables and citations.

## Compare across sources
kind: step
do: Tick all your sources. Ask the matrix prompt, then the agreements-and-disagreements prompt. Save both to notes.
check: The notebook tends to make papers sound as if they agree. Look for differences in learners, tasks and measures that it smoothed over.

## Check every citation you will use
kind: step
do: For each claim you plan to put in your review, open the citation and classify it: **supported**, **partly supported**, or **not supported**. Keep only supported claims, with page numbers.
check: Never cite Gemini Notebook. Cite the original paper, at the page you checked.

## Use the Studio panel to review — not to replace reading
kind: step
do: **Mind Map** shows the themes across your sources as a branching diagram. **Reports** produce a briefing document or study guide. **Flashcards** and **Quizzes** test your own understanding. **Audio Overview** turns the sources into a spoken discussion you can listen to.
check: These are summaries of summaries. Use them to see the shape of the field; check anything you will rely on against the source.

## Write the review yourself
kind: step
do: Organise your review **by theme or by question, not one paragraph per paper**. For each theme: what the studies found, where they differ, and why that matters for your project.
check: A good review ends with the gap your project addresses.

## Share with your group, if you have one
kind: step
do: If you work in a group, share the notebook so everyone works from the same sources. Personal accounts can share a notebook with up to 50 people.

## Prompts to copy
kind: section
Replace the parts in [square brackets].

## Role for Configure Chat
kind: prompt
```text
You are a careful research assistant helping a graduate student write a literature review in applied linguistics on [your topic]. Answer only from the selected sources. For every claim, cite the source. If the sources do not say something, say "the sources do not say". Do not combine findings from different studies into one claim unless you name each study.
```

## Extract one study
kind: prompt
```text
For the selected source only, give:
1. Full reference as printed in the paper (authors, year, title, journal, volume, pages)
2. Research question(s) or aim
3. Participants: number, age, proficiency, first language, setting
4. Design and method (quantitative / qualitative / mixed; instruments; duration)
5. The digital material or AI tool studied, and how learners used it
6. Main findings, with the numbers the authors report
7. Limitations the authors themselves mention
Quote the key sentence for findings 6 and 7.
```

## Build a literature matrix
kind: prompt
```text
Make a table with one row per source and these columns: Author (Year) | Learners and setting | Material or tool | Method | Outcome measured | Main finding | Limitation. Keep each cell under 20 words. If a source does not report something, write "not reported".
```

## Agreements, disagreements, gaps
kind: prompt
```text
Across the selected sources:
1. Where do the findings agree? Name the studies.
2. Where do they disagree or differ? Explain whether the difference could come from different learners, tasks, tools or measures.
3. What do none of the sources study? List three gaps.
Do not smooth over differences.
```

## Test my research question
kind: prompt
```text
My research question is: [your question]. Based only on the selected sources:
1. Which sources are most relevant to it, and why?
2. Has any source already answered it? If so, how is my question different?
3. Which method in these sources could I adapt for my study?
```

## Explain a method I do not understand
kind: prompt
```text
In [Author (Year)], explain the [statistical test / coding procedure / instrument] the authors used, in plain language, as if to a teacher with no statistics background. Then explain what the reported result means and what it does not mean. Cite the passage.
```

## What Gemini Notebook cannot do
kind: card
- It cannot tell you whether a source is peer-reviewed, influential or methodologically sound.
- It only knows your sources. Ask about something they do not cover and it should say so — check that it does.
- From YouTube it imports only the transcript; from a web page only the text — no images, no embedded video.
- Paywalled web pages cannot be added. Download the PDF through the library instead.
- Its summaries can merge two studies' findings into one sentence. Always check citations before you reuse a claim.

## Your literature matrix
kind: card
Copy this table into your proposal and fill one row per source.

| Author (Year) | Learners & setting | Material / tool | Method | Outcome | Main finding | Limitation | Why it matters for my project |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
