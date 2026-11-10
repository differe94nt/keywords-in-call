# Build it with AI

You have your first idea and you have read the research. Now **revise the plan**, then **guide** an AI to build it — you make the design decisions; the AI does the construction. Use the free versions: **Gemini first**, then Claude or ChatGPT if you need a second attempt.

<!--
HOW TO EDIT
  ## Title   kind: step · prompt (fenced ``` block) · card · section
-->

## Five steps
kind: section

## Revise your draft · version 1
kind: step
do: Go back to your version 0. For each part, write **keep**, **change** or **drop** — and name the study behind every change. Keep version 0 unchanged; your portfolio needs both. If you matched websites on the Activity board, decide here: build your own page, use an existing tool, or combine them.

## Write the specification
kind: step
do: Fill in the specification below. The more precise it is, the less you fix later.

## Generate
kind: step
do: Paste the builder prompt, your specification and the add-on for your skill into Gemini with **Canvas** selected. Open **Preview**.
tip: In Claude, turn on **Settings → Capabilities → Cloud code execution and file creation** first. In ChatGPT, copy the code into a plain-text file, save it as `activity.html` and open it in Chrome.

## Test it as a learner
kind: step
do: For closed questions, try a right answer, a wrong answer and no answer. For open speaking or writing tasks, walk through the steps, hints, criteria and checklist instead — the page cannot judge free answers. Try it on a phone, and for listening, play the audio on the device you will present with. Then send the test prompt below.
check: Are all answer keys correct? Does the activity do what your plan says — or something easier to build?

## Revise and save each version
kind: step
do: Ask for specific changes, one at a time. Save every version and note what you changed and why. The before-and-after is evidence for your presentation and your portfolio.

## The prompts
kind: section
Replace everything in [square brackets].

## Your specification
kind: prompt
```text
Skill: [listening / speaking / reading / writing]
Learners: [age, level, setting, one detail that matters]
Learning goal: by the end, learners can [observable goal]
Activity steps: [your revised steps from version 1]
Research basis: [author and year] — [the design decision it supports]
Where AI helps: [preparing material / during the activity / feedback]
Success check: [what learners do at the end, with new content]
```

## Builder prompt
kind: prompt
```text
You are helping a teacher build a classroom activity. Use my specification below exactly; do not change the learning goal or the steps.

[PASTE YOUR SPECIFICATION]

Build ONE self-contained HTML page that:
1. Shows the learning goal in learner-friendly English.
2. Runs the activity steps in order, with clear instructions on each screen.
3. For closed-answer items, uses teacher-checked answer keys, offers an optional hint first, and explains the answer. For open speaking and writing tasks, provides criteria, an example and a self/peer checklist instead; it does not claim to score free speech or diagnose a learner's text.
4. Ends with a final independent task on new content, with hints and model answers unavailable.
5. Has a "For the teacher" section with the answer key and a 5-line lesson plan (timing, grouping, materials).
Requirements: no external libraries, images or links; no AI calls; no collection or storage of learner data; large readable text; works with keyboard only; does not rely on colour alone; works on a phone.
After the code, list the checks you made on every answer key.
```

## Add-on · listening
kind: prompt
```text
Listening: use the browser's built-in speech synthesis (Web Speech API) to read each audio chunk aloud, with Play, Slower and Replay buttons. Hide the transcript until after the learner answers. Write the script as natural speech, with contractions and short sentences.
```

## Add-on · speaking
kind: prompt
The page itself makes no AI calls, so it cannot hold a real conversation. It prepares learners; talking to an AI partner is a **separate step** in another tool, with the instructions below.
```text
Speaking: the page prepares learners to speak with a partner rather than talking to them. Include a role card for each partner, 4–6 useful phrases with example sentences, a planning space, and a "listener checklist" with one follow-up question to ask. If I want an AI conversation partner, write its instructions separately: replies of one or two sentences, one question per turn, and when the learner makes an error, ask a clarification question or give a clue instead of correcting it.
```

## Add-on · reading
kind: prompt
```text
Reading: show the text with [6–8] target words underlined. Clicking a word opens a short, level-appropriate definition and a simple picture drawn with inline SVG (no image files). After reading, add questions by subskill: one main idea, one detail, one inference, one vocabulary in context. Each question must need the text to answer.
```

## Add-on · writing
kind: prompt
```text
Writing: the page guides learners through writing a short [genre] paragraph on [topic], then a self-check on ONE pattern: [e.g. verb tense]. Provide a checklist and two example sentences, and show learners WHERE to look in their own writing without correcting it for them. Finish with a short new writing task on a different topic.
```

## Test it before you present
kind: prompt
```text
Review the page you built as a strict teacher and as a learner at [level]:
1. Check every answer key for closed items and list any errors. For open tasks, check that the criteria, example and checklist match the learning goal, and that the page never pretends to grade free answers.
2. List any words or structures above [level].
3. Check: keyboard use, text size, contrast, phone layout, anything that relies on sound or colour alone. For listening, tell me which parts I must check by ear on a real device.
4. Does every step practise [learning goal]? Which step practises something else?
Fix the three most important problems and tell me exactly what you changed.
```

## Keep a version log
kind: card
Copy this table into your group document — it becomes the "what we tried" part of your presentation.

| Version | What we asked the AI | What came back | What we changed, and why |
|---|---|---|---|
| v1 | | | |
| v2 | | | |
