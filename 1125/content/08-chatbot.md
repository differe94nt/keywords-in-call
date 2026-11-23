# Build a chatbot

Now turn the readings into practice. **Mizou** lets a teacher build a chatbot that learners talk to — with read-aloud and voice input, so it can run listening and speaking tasks. **Yoodli** is an AI speaking coach for adults: you use it yourself to rehearse a talk or a role-play and get feedback on your delivery.

<!--
HOW TO EDIT
  ## Title   kind: card · step · prompt (fenced ``` block) · section · checklist · questions
  Platform details were checked on 23 Nov 2026 — recheck before each semester.
-->

## Design rules from the readings
kind: section
Six findings to build into your bot. Each one comes from a paper on the earlier pages.

## Let learners choose and pace
kind: card
Topic choice, control over response time and the option to ask for clarification were built into the GPT examiner. Decide in advance how clarification requests count — they went with lower scores.
refs: gptspeak

## Design the feedback by level
kind: card
Feedback on the **task** (what was said), the **process** (how to improve) and **self-regulation** (how to plan and monitor next time). Test and revise the bot's instructions several times.
refs: ylgenai

## Keep a human in the loop
kind: card
Chatbots raise willingness to communicate, but do not build the whole repertoire of interaction skills. Pair bot practice with face-to-face talk, and check what the bot says.
refs: goh2025

## Check AI-written listening items
kind: card
AI writes good levelled scripts but weak items: long, with overlapping options, sometimes answerable without listening.
refs: llmlisten

## Make listening input realistic
kind: card
Spoken features, more than one accent, visuals, varied tasks, bottom-up and top-down processing, and a metacognitive step.
refs: lcbook

## Name the purpose
kind: card
Is the bot's feedback assessment **of**, **for** or **as** learning? The answer decides what evidence would show the bot works.
refs: argval

## The two platforms at a glance
kind: section
Checked on 23 November 2026. Both change often — check the pricing and terms pages before class.

| | Mizou | Yoodli |
|---|---|---|
| Who builds | The teacher builds a bot | Ready-made practice; custom role-plays mostly on organisation plans |
| Who uses it | Learners, through a link, **no learner account** | The account holder — you |
| Voice | Read-aloud and voice input on all plans | Live spoken role-plays, speeches and interviews; camera optional |
| Feedback | The bot's replies; rubric grading on paid plans | Delivery analysis, e.g. filler words and pacing; pronunciation feedback can be switched on |
| Free plan | 10 student sessions per day; no rubrics, timer or knowledge files | **5 practice sessions in total**, not per month |
| Age | Built for schools; the terms page was offline when we checked | Terms: **18 and over** |
| Data | Says student chats are not used to train AI | Recordings may be used to train models unless you opt out in settings |
Sources: [Mizou pricing](https://mizou.com/pricing) · [Mizou privacy policy](https://help-mizou.notion.site/Privacy-Policy-055351d6afe94831a28ec7b29375d8fa) · [Yoodli pricing](https://yoodli.ai/pricing) · [Yoodli terms](https://yoodli.ai/tos)

## Mizou · build a listening or speaking bot
kind: section
Mizou's own help centre was offline when we checked, and the site now says *Mizou is now part of MeltingSpot*. The steps below follow the current site and recent teacher guides; labels may have moved.

## Sign up and look at an example
kind: step
do: Create a free teacher account at [mizou.com](https://mizou.com/education). Then open the [example module](https://mizou.com/module/1706790030516x865778483436453900) **while logged in** — logged-out visitors are sent to the home page.

## Start a new bot
kind: step
do: Choose **Custom** (start from scratch), a **Template**, or **AI-Generated** (enter a grade and learning objectives, then click *Get Ideas*). For this class, choose **Custom**.

## Fill in the fields
kind: step
do:
- **Standards:** title, grade level, learning objectives.
- **AI Instructions** and **Rules:** paste and edit a template below. Keep the instructions short — teacher guides report a limit of about 1,000 characters.
- **Customization:** the bot's name and a welcome message, which is the first thing learners see.
- **Tools:** turn on **Audio**, so learners can play the bot's messages aloud and answer by microphone.
tip: **Generate all fields** fills everything with AI — useful for a first draft, but rewrite it to match your design.

## Test it as a learner
kind: step
do: Run it on your phone with the audio on. Try a good answer, a weak answer, an off-topic answer and a request for help. Does the bot follow every rule?

## Publish and share
kind: step
do: Click **Publish** and choose whether the bot is public or visible only to you and your students. Start a session and copy its link; learners open it, type a first name and start. They do not need accounts.

## Read the transcripts
kind: step
do: In your bot's session list, open each learner's transcript. On paid plans Mizou also suggests a rubric grade. Read the transcripts yourself — this is your evidence of what the bot actually did.

## Mizou template · listening
kind: prompt
Read-aloud shows the text as well as playing it, so ask learners to **play first, then read**. This is a practice tool, not a listening test.
```text
You are a listening partner for [level, e.g. CEFR A2] learners of English.
Goal: learners understand the gist and key details of short spoken messages about [topic].
Each round:
1. Ask the learner to press play and listen before reading.
2. Say a 50–70-word message in natural spoken English (contractions, a filler, a self-correction).
3. Ask one gist question. After the answer, ask one detail question.
4. If wrong, give a hint about where to listen; do not give the answer at once.
5. After 3 rounds, ask: "What helped you understand? What will you listen for next time?"
Use words at [level]. One question per turn.
```

## Mizou template · speaking
kind: prompt
Based on the design choices in Aryadoust et al. (2026) and the feedback levels in Aryadoust & Zakaria (2026).
```text
You are a friendly speaking partner for [learners, level].
Goal: learners can [e.g. describe a plan and give two reasons].
1. Offer three topics; the learner chooses one.
2. Ask one short question per turn (max 2 sentences). Ask the learner to answer by microphone.
3. The learner may ask you to repeat or explain at any time; never penalise this.
4. When the learner makes an error, ask a clarification question or give a clue; do not give the correct sentence.
5. After 6 turns, give feedback in three short parts: Task (what you said well), Process (one thing to improve and how), Next time (one planning tip).
Never ask for personal information.
```

## Rules to add in either bot
kind: prompt
```text
Stay on the topic of [topic]. Use English at [level]. Keep every reply under 60 words.
If the learner writes in another language, answer briefly in simple English and continue.
Do not ask for names, schools, addresses or photos.
```

## Yoodli · rehearse your own speaking
kind: section
Use Yoodli to rehearse **your** presentation of this week's paper — not with school students: its terms require users to be 18 or over.

## Sign up
kind: step
do: Sign up at [app.yoodli.ai](https://app.yoodli.ai/home). The free plan gives **five practice sessions in total**; any speech, interview or role-play over 30 seconds counts as one.

## Check your settings first
kind: step
do: In settings, choose the **practice language** (English US, UK or Australian) and turn on **pronunciation feedback** if you want it. Opt out of your recordings being used to train Yoodli's AI if you prefer, and keep recordings private.

## Practise
kind: step
do:
- **Speech:** practice → speech → *Start*, speak after the countdown, then *Stop*.
- **Role-play:** practice → conversation → choose a scenario or *Personalize your conversation*, allow the microphone, *Start* and talk.
- **Interview:** enter a role, choose the interviewer's manner, optionally add your own questions.

## Read the analysis
kind: step
do: Click **View Analysis**. Look at filler words, pacing and word choice, and ask for an AI follow-up question if you want Q&A practice. Note one thing to change, then try again — that before-and-after is evidence for your portfolio.

## Share or delete
kind: step
do: In the **Recording Library**, use the three-dot menu to copy a share link, download or delete a recording.
tip: Yoodli has a **Builder** for custom role-plays, but personas, goals and custom rubrics are on Business and Enterprise plans. Check what your account shows.

## In class today
kind: section

## Build, swap, review
kind: step
time: 40 minutes
do:
- **Pairs (20 min):** build one Mizou bot — listening or speaking — from the templates. Write down which paper supports each design choice.
- **Swap (10 min):** use another pair's bot as a learner, with audio on. Note one thing that worked and one rule the bot broke.
- **Review (10 min):** read your bot's transcripts and revise its instructions once. Keep both versions.

## Rehearse
kind: step
time: 15 minutes
do: Each person rehearses a **two-minute talk** on their paper in Yoodli — research question, method, one finding, one implication. Use one free session only, and keep the analysis for your portfolio.

## Before you use either tool
kind: checklist
- No real learner names, voices or work go into either tool without consent
- Age rules checked for the learners who would use the bot
- The bot's instructions forbid asking for personal information
- I read the transcripts and checked what the bot said
- I can name the paper behind each design choice

## Evaluate your bot
kind: questions
- What is your bot's purpose — assessment of, for or as learning — and what evidence from the transcripts shows it served that purpose?
- Which of the six design rules did your bot follow, and which did it break?
- What would you change before using it with real learners?
