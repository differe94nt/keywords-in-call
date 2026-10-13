# Research track

Your research is about **language-teaching digital material design** or **AI in language teaching**. You ask a focused question, collect data from real participants, and report what you found — honestly, including what a small pilot cannot tell you.

<!--
HOW TO EDIT
  ## Title   kind: checklist | section | card | step | questions
  checklist / questions: "- " lines become ticks / numbered questions
  refs: ids from refs.md, separated by |
-->

## Midterm proposal · due 11/04
kind: checklist
Tick each item when your draft actually contains it.
- **Topic** within digital material design or AI in language teaching, with your target learners named
- **Literature review of 5 sources** — at least four peer-reviewed; organised by theme, not one paragraph per paper
- **At least one research question**, specific enough that data could answer it
- **Method:** quantitative *or* qualitative, with the reason for your choice
- **Participants:** who, how many, how you will reach them, and their consent
- **Instruments:** test, questionnaire, interview questions or task — attached as a draft
- **Procedure and timeline** that finishes data collection before 12/16
- **Analysis plan:** what you will count, compare or code
- **References** in APA 7, each one checked against its DOI or database record

## Final presentation · 12/16 or 12/23
kind: checklist
- **Literature review of 5 sources**, updated with anything you found during the project
- **Research question(s)** — say if you revised them and why
- **Method** as actually carried out, including what changed from the proposal
- **Results** — at least pilot results, shown in a table or chart with the numbers behind it
- **Discussion:** what the results suggest, what they cannot show, and the next study you would run
- **How the project connects to this course** — which week's concepts it builds on

## From topic to research question
kind: section
A topic names an area; a question names who, what and how you will know. Each pair below starts from a topic classmates are already exploring.

## Multimodal vocabulary
kind: card
avoid: Does multimodal input help vocabulary learning?
example: Do Grade 10 EFL learners recall more target words one week later after studying with picture-plus-audio flashcards than with text-only flashcards?
why: The better version names the learners, the comparison, the outcome and the timing — so it tells you what data to collect.

## Learners with hearing impairments
kind: card
avoid: How can AI help hearing-impaired students learn English?
example: How do three Deaf or hard-of-hearing secondary learners describe their use of AI-generated captions and visual glossaries during a reading lesson, and what difficulties do they report?
why: A qualitative question suits a small, specific group. It asks about their experience rather than assuming what helps. Plan consent and communication access (for example a sign-language interpreter) from the start.

## AI-made learning games
kind: card
avoid: Are AI games good for learning?
example: After two 15-minute sessions with a teacher-built vocabulary game, do Grade 5 learners score higher on a picture-matching test, and how do they rate their enjoyment?
why: Measures learning and enjoyment separately — enjoyment alone is not evidence of learning. With learners under 18 you need school and parent or guardian consent, and the game must not send their data to an AI service.

## Quantitative or qualitative?
kind: section

| | Quantitative | Qualitative |
|---|---|---|
| **Answers** | How much? Is there a difference? Is there a relationship? | How? Why? What is it like for these learners? |
| **Typical data** | Test scores, questionnaire ratings, time on task, counts | Interviews, open-ended responses, observation notes, learner texts |
| **Pilot size** | Small groups are fine for a pilot (for example 8–20), but treat any difference as preliminary | 3–8 participants can be enough if you talk to them in depth |
| **You report** | Descriptive statistics, a test of difference, an effect size | Themes with quotations, and how you reached them |
| **Common trap** | Calling a small pre–post gain "proof" without a comparison | Listing quotations without analysing them |

## Analysing numbers: a short guide
kind: section
You do not need advanced statistics for a pilot. You need to describe your data honestly and choose a test that matches your design. Free tools: [JASP](https://jasp-stats.org/) and [jamovi](https://www.jamovi.org/) (point-and-click, free), or Google Sheets for descriptive statistics.

## Describe first
kind: step
do: For every measure, report the number of participants (*n*), the mean and standard deviation, and the minimum and maximum. For Likert items, also report the median and how many people chose each option.
check: Look at the raw numbers before any test. One participant scoring 0 because they missed the session changes everything in a small sample.

## One group, before and after
kind: step
do: Use a **paired-samples t-test**. If the sample is very small or scores are clearly not normally distributed, use the **Wilcoxon signed-rank test** instead.
check: Without a comparison group, a gain could come from practice, the second test being easier, or ordinary teaching. Say so in your discussion.

## Two groups compared
kind: step
do: Use an **independent-samples t-test**, or the **Mann–Whitney U test** for small or skewed samples. Check the groups were similar before the treatment.
check: If groups were not randomly assigned, report how they differed at the start.

## Report an effect size
kind: step
do: Report Cohen's *d* alongside the test. For L2 research, Plonsky and Oswald suggest roughly 0.40 / 0.70 / 1.00 as small / medium / large for between-group comparisons, and 0.60 / 1.00 / 1.40 for within-group (pre–post) comparisons.
check: An effect size tells you *how big*; the *p* value only tells you how surprising the result would be if there were no real difference. With a pilot sample, a large effect can still be non-significant — report both.
refs: plonsky_oswald2014

## Questionnaires with Likert items
kind: step
do: Report each item's distribution (how many chose 1–5). If several items measure one idea, average them into a scale score and check that they hang together (Cronbach's alpha in JASP or jamovi).
check: Do not treat one item as a whole construct, and do not call agreement "learning" — it is perception.

## Analysing words: thematic analysis
kind: section
For interviews and open-ended answers, follow the six phases of thematic analysis. Keep a table of codes with the quotations that support each one.
refs: braun_clarke2006

## Six phases
kind: card
- **Familiarise:** read every response twice; note first impressions
- **Code:** label meaningful pieces of data (for example "captions too fast")
- **Search for themes:** group codes into candidate themes
- **Review themes:** check each theme against the data — does it hold?
- **Define and name:** write one sentence saying what each theme is about
- **Write up:** present each theme with two or three quotations and your interpretation
refs: braun_clarke2006

## Ethics and data
kind: card
- Get **informed consent** — and for learners under 18, permission from the school and a parent or guardian.
- **Anonymise** names, schools and anything identifying before analysis or presentation.
- **Do not paste participants' data into free AI tools.** Google's terms for its free AI Studio tier, for example, say human reviewers may read inputs and ask users not to submit personal information. See *Issues to think through* in the AI materials studio.
- Store data in a private folder, and delete it when the project ends unless participants agreed otherwise.

## Questions to test your design
kind: questions
- Could someone else repeat your study from your method section alone?
- What result would make you change your mind about your research question?
- How will you know a difference came from your material and not from something else?
- Are your participants the learners your question is about?
- What is the smallest version of this study you could finish before 12/16?
