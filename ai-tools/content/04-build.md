# Build with a language model

A language model builds what you describe — so the quality of the material depends mostly on the quality of your **specification**. These prompts work in Gemini Canvas, Claude, ChatGPT and Google AI Studio. Each one asks for the things teachers usually forget: the learner, the goal, the answer key, accessibility, and no data collection.

<!--
HOW TO EDIT
  ## Title   kind: step · prompt (fenced ``` block) · card · section
-->

## Five steps for any material
kind: section

## Specify
kind: step
do: Write down the learners (age, level, first language, setting), one learning goal, the theory behind the activity, the length, and the format. Use your learner analysis — the more precise it is, the better the first draft.

## Generate a first draft
kind: step
do: Paste the matching prompt below with your details filled in. Ask for one material at a time.

## Test it like a learner
kind: step
do: Use it yourself: give a correct answer, a wrong answer and no answer; try it on a phone; try it with the sound off.
check: Is every answer key correct? Is the language at the right level? Does anything depend on audio alone?

## Revise
kind: step
do: Ask for specific changes ("make the sentences shorter", "add a hint before showing the answer", "larger buttons"). In Google AI Studio you can use annotation mode — point at part of the screen and describe the change.
tip: Keep each version. The before-and-after is good evidence for your portfolio.

## Show and share
kind: step
do: Share a link (Canvas **Share & export**, a published artifact, or a deployed AI Studio app), or download the HTML file. For class, put the link in a QR code and bring a PDF or screenshot backup.

## Prompts to copy
kind: section
Replace everything in [square brackets]. Delete lines that do not apply.

## Worksheet or handout
kind: prompt
```text
Create a printable worksheet for [age, level, e.g. Grade 5 A1 / university B1] learners of English in [setting, e.g. Taiwan].
Learning goal: by the end, learners can [observable goal].
Theory: design it using [e.g. scaffolding — support that is gradually removed].
Structure: a short model example → 3 guided items with a word bank → 3 items without the word bank → 1 short personal task.
Use only vocabulary at [level]; keep instructions under 15 words each.
Add a separate answer key for the teacher.
Format for A4, large readable font, no decorative images.
List any assumptions you made about the learners.
```

## Multimodal vocabulary set
kind: prompt
```text
Create a set of [8] vocabulary cards for [learners] on the topic [topic].
For each word give: the word, part of speech, a simple definition at [level], one example sentence about the learners' everyday life, a description of a picture that shows the meaning clearly, and a one-line caption for that picture.
Follow multimedia learning principles: the picture must show the meaning, not decorate; put the word next to its picture; no extra text that repeats the audio word for word.
Make sure every piece of information is available visually, so the set works for learners who are Deaf or hard of hearing.
Then suggest one short activity where learners use the words to describe something to a partner.
```

## Interactive practice activity or learning game
kind: prompt
```text
Build a self-contained interactive HTML learning game for [learners, age, level].
Learning goal: [observable goal]. Content: use ONLY these items, written by me: [paste your items and correct answers].
Game: [e.g. match each picture description to the word / drag words to complete sentences / choose the correct response in a short dialogue].
Requirements:
- Learners try first; feedback comes after each answer and explains why.
- An optional hint button before the answer is shown.
- A final round with new items and no hints, so I can check independent use.
- Score shown at the end; no timer pressure unless I ask.
- Large text, high contrast, works with keyboard only, does not rely on colour or sound alone.
- No external libraries, no AI calls, no tracking, and no collection or storage of learner data.
- A printable version of the items and answer key.
After building, list how you tested correct, wrong and empty answers.
```

## Show your teaching materials interactively
kind: prompt
```text
Build a single-page interactive presentation (one HTML file) that showcases my teaching design to classmates.
Sections, one screen each, navigable with arrow keys and buttons:
1. Title: [lesson title], my name, target learners
2. The learners: [3–4 key facts from my learner analysis]
3. The learning goal and the theory behind it: [goal]; [theory with author and year]
4. The lesson stages with timing: [paste my 20-minute plan]
5. The materials: embed or link [my worksheet / game / images] so the audience can try them
6. How AI was used and how I checked it: [details]
7. What I would change after testing: [details]
Keep text short on each screen; use large fonts, alt text for every image, and no external services.
Add a printable handout version of the whole presentation at the end.
```

## Your portfolio as an HTML presentation
kind: prompt
```text
Build my end-of-semester learning portfolio as one self-contained HTML file with slide-style sections navigated by arrow keys, buttons, and a contents menu.
Sections:
1. Cover: name, course "英語數位教材與教學", semester
2. Where I started: [my answers]
3. What I learned — three concepts, each with an example from my work: [notes]
4. What I tried — tools and methods, what worked and what did not: [notes]
5. Three artifacts, each with an image and a caption explaining what it shows: [file names and captions]
6. Feedback I received and what I changed: [quotes, anonymised]
7. My final project: role, best decision, one change: [notes]
8. AI-use statement: [which tools, for what, how I checked]
9. Looking ahead: [notes]
Design: calm colours, large readable text, alt text for every image, works on a phone, prints one section per page.
Do not invent anything I did not provide — leave a clearly marked placeholder instead.
No external libraries, no tracking.
```

## Test and improve what was built
kind: prompt
```text
Review the material you just built as a strict teacher and as a learner at [level]:
1. Check every answer and answer key; list any errors.
2. List any words or structures above [level].
3. Check accessibility: keyboard use, text size, contrast, anything that relies on sound or colour alone.
4. Check the learning goal: does each task actually practise [goal]?
Then fix the three most important problems and show me what you changed.
```

## About Google AI Studio's Build mode
kind: card
- Build mode turns a description into a full web app you can preview, refine by chat or by pointing at the screen, and deploy.
- **It is a tool for adults.** The terms require you to be 18 or over and do not allow apps "directed towards or likely to be accessed by" anyone under 18. For school-age learners, ask for a version with **no AI calls**, download it, and use that.
- On the free tier, human reviewers may read what you submit. Do not include learner names, writing or recordings.
link: [Build mode documentation](https://ai.google.dev/gemini-api/docs/aistudio-build-mode) · [Gemini API terms](https://ai.google.dev/gemini-api/terms)

## Showing materials in class
kind: card
- **Link + QR code** so classmates can open the material on their phones.
- **A backup that needs no internet:** the downloaded HTML file, a PDF, or screenshots.
- **Let the audience try it.** Two minutes of classmates using your game says more than five slides about it.
- **Show the before and after** of one revision — it makes your design thinking visible.
