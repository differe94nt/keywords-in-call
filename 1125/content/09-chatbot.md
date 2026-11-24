# Build a chatbot

Now turn the readings into practice. **Mizou** lets a teacher build a chatbot that learners talk to — with read-aloud and voice input, so it can run listening and speaking tasks. **Yoodli** runs spoken AI role-plays, interviews and speeches with feedback, and lets learners practise in **US, UK or Australian English**. Both can be set up as tasks. Before building, decide what the bot's assessment is **for**.

<!--
HOW TO EDIT
  ## Title   kind: card · step · prompt (fenced ``` block) · section · checklist · questions · reveal
  Platform details were checked on 23–24 Nov 2026 — recheck before each semester.
-->

## Assessment of, for or as learning?
kind: section
The same chatbot can serve three different purposes. Each purpose needs different features in the bot and different evidence that it works.
refs: wiliam2011 | earl2013 | argval

| | Assessment **of** learning | Assessment **for** learning | Assessment **as** learning |
|---|---|---|---|
| Main purpose | Judge, rank or certify what learners can do | Guide the next step in teaching and learning | Help learners monitor and regulate their own learning |
| Also called | Summative | Formative | Self-assessment, self-regulation |
| Who uses the evidence | Teacher, school, others outside class | Teacher and learners, during the course | Mainly the learner |
| When | At the end of a unit or course | During learning, often | Throughout, built into the task |
| Example in a speaking class | A recorded oral exam with a rubric | A practice talk with feedback the class acts on | Learners set a goal, check their own recording against criteria, plan the next try |
| What the bot does | Asks the same questions of everyone and scores against a rubric | Gives feedback that says what to do next, and lets learners try again | Asks learners to set a goal, judge their own answer and plan the next attempt |
| What the bot should keep | Comparable transcripts and scores | Each attempt, the feedback and the next attempt | The learner's goals, self-ratings and reflections |
| Validity question | Are the scores accurate, fair and consistent? | Did the teacher or learner act on the evidence, and did the next attempt improve? | Can learners judge their own work against the criteria? |
| In Mizou | Rubric grading (paid plans) and transcripts | The bot's feedback rules; transcripts for the teacher | A goal-setting opening and a reflection at the end |
Sources: Black & Wiliam (1998); Wiliam (2011), including the definition by Black et al. (2004) he quotes; Earl (2013); Lee (2007); Aryadoust & Zakaria (2026).

## The key distinction
kind: card
Wiliam (2011) separates two things that are often mixed up. **For** and **of** learning are about the **purpose** an assessment was designed for. **Formative** and **summative** are about the **function** it actually serves. A test designed to rank can still be used formatively, and a practice quiz can end up only producing a mark. An assessment is formative only when the evidence is **used** to decide the next step.
refs: wiliam2011 | blackwiliam1998

## Which one is your bot?
kind: reveal
- **A bot that asks ten questions and reports a score** — assessment *of* learning. You need consistent questions, a clear rubric, and a check that the scores agree with a human rater (Aryadoust et al., 2026, found that GPT and human ratings differed significantly on 3 of 8 scoring categories).
- **A bot that gives a hint and asks the learner to try again** — assessment *for* learning, but only if the learner's second attempt uses the hint. Read the transcripts to see.
- **A bot that opens with "What is your goal today?" and closes with "How did you do, and what will you try next time?"** — assessment *as* learning. The evidence is in the learners' own judgements and plans.
refs: gptspeak | wiliam2011 | earl2013

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
Decide whether the bot's assessment is **of**, **for** or **as** learning — see the table at the top of this page. The purpose decides what evidence would show the bot works.
refs: argval

## The two platforms at a glance
kind: section
Checked on 23–24 November 2026. Both change often — check the pricing and terms pages before class.

| | Mizou | Yoodli |
|---|---|---|
| Who builds | The teacher builds a bot | Ready-made role-plays, interviews and speeches; anyone can build custom role-plays in the **Builder** |
| Who uses it | Learners, through a link, **no learner account** | Each learner with **their own account**; sharing a custom role-play by link is Enterprise only |
| English varieties | Set the variety in the bot's instructions (for example, British spelling); Mizou does not say which accent its read-aloud voice uses | Practice language **English – USA, UK or Australia**, chosen before each session (and 26 other language options) |
| Voice | Read-aloud and voice input on all plans | Live spoken role-plays; each AI persona has its own voice, chosen in the Builder |
| Feedback | The bot's replies; rubric grading on paid plans | Delivery analysis, such as filler words and pacing; optional pronunciation feedback aimed at being understood |
| Free plan | 10 student sessions per day; no rubrics, timer or knowledge files | **5 sessions in total** (Starter); any session over 30 seconds counts |
| Age | Built for schools; the terms page was offline when we checked | Terms: **18 and over** |
| Data | Says student chats are not used to train AI | On Starter and Pro, session data **may be used** to improve the platform; excluded on Advanced and above |
Sources: [Mizou pricing](https://mizou.com/pricing) · [Mizou privacy policy](https://help-mizou.notion.site/Privacy-Policy-055351d6afe94831a28ec7b29375d8fa) · [Yoodli pricing](https://yoodli.ai/pricing) · [Yoodli terms](https://yoodli.ai/tos) · [Yoodli: language and localization](https://support.yoodli.ai/en/articles/15346192-yoodli-language-localization-overview) · [Yoodli: customizing practice](https://support.yoodli.ai/en/articles/9628260-customizing-practice)

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

## A task bot
kind: card
For a bot built as a **task** — with an information gap, a decision and a language focus at the end — use the template on the [Tasks, problems and projects](#p-1) page.

## Rules to add in either bot
kind: prompt
```text
Stay on the topic of [topic]. Use English at [level]. Keep every reply under 60 words.
If the learner writes in another language, answer briefly in simple English and continue.
Do not ask for names, schools, addresses or photos.
```

## Yoodli · English varieties and AI role-plays
kind: section
Yoodli's strength for a language class is **spoken role-play in a chosen variety of English**, with feedback after each session. It suits **adult learners (18 and over)**, such as university students — its terms do not allow younger users. Checked on 24 November 2026.

## Choose the English variety
kind: card
Before each session, choose the practice language from the **language menu at the bottom left of the video preview**: **English – USA**, **English – UK** or **English – Australia**. Yoodli also lists 26 other language options.
- The choice changes the **transcript**, the **AI partner's replies** and the **feedback** to match that variety.
- It does **not** change the AI voice's accent: the voice belongs to the role-play's **persona**.
link: [Yoodli: language and localization](https://support.yoodli.ai/en/articles/15346192-yoodli-language-localization-overview)

## Voices come with personas
kind: card
In the **Builder**, every AI persona has a name, role, manner and a **voice**. Yoodli picks a voice from its standard set, and you can choose another. To hear different voices, build or choose personas with different voices — Yoodli does not publish a list of accents.
link: [Yoodli: personas](https://support.yoodli.ai/en/articles/18419351-personas-create-with-ai) · [Yoodli: customizing practice](https://support.yoodli.ai/en/articles/9628260-customizing-practice)

## Pronunciation feedback: being understood
kind: card
Learners can turn on **pronunciation feedback** in their personal settings. Yoodli says it does **not** aim to remove an accent, but to show what would make the speaker **easier to understand**. It switches itself off if it detects a native speaker.
link: [Yoodli: personal settings](https://support.yoodli.ai/en/articles/10055670-personal-settings)

## Limits to plan around
kind: card
- **Five sessions in total** on the free Starter plan — any session over 30 seconds counts. Plan each one.
- **18 and over** only.
- A teacher cannot share a custom role-play by link unless the school has an **Enterprise** plan. On free accounts, each learner builds the role-play from your written instructions.
- On Starter and Pro, session data **may be used** to improve Yoodli. Recordings are **private** until shared.
link: [Yoodli pricing](https://yoodli.ai/pricing) · [Yoodli terms](https://yoodli.ai/tos)

## Task 1 · Same conversation, three varieties
kind: step
time: 3 sessions
do:
- **Pre-task:** choose one role-play — a job interview or a service encounter. Write down three phrases you plan to use.
- **Task:** do it three times, with the practice language set to **US**, then **UK**, then **Australia**. Keep the same goal each time.
- **Report:** compare the three transcripts and feedback reports. Which words, spellings or phrases changed? What did the feedback flag differently?
- **Language focus:** choose two expressions to keep, and say in which variety each one is more typical.
tip: This links to **L7 Accent compare** on the 11/11 board, and to the listening-materials principle of exposing learners to more than one variety (Zhai et al., 2026).

## Task 2 · Be understood, then try again
kind: step
time: 2 sessions
do:
- Turn on **pronunciation feedback**. Give a **one-minute** talk on a topic you know.
- Click **View Analysis**. Choose **one** point that would make you easier to understand.
- Give the same talk again. Compare the two reports — that before-and-after is assessment **for** learning, and your note on it is assessment **as** learning.

## Task 3 · Build a persona (for the teacher)
kind: step
do: In the **Builder**, create a role-play with a persona whose voice differs from Yoodli's default. Write the persona's role, manner and goal. Then write the instructions your learners would follow to build the same role-play in their own accounts.
tip: Personas, goals and custom rubrics for a whole class are on Business and Enterprise plans. Check what your account shows.

## In class today
kind: section

## Build, swap, review
kind: step
time: 40 minutes
do:
- **Pairs (20 min):** build one Mizou bot — listening or speaking — from the templates. Write down which paper supports each design choice.
- **Swap (10 min):** use another pair's bot as a learner, with audio on. Note one thing that worked and one rule the bot broke.
- **Review (10 min):** read your bot's transcripts and revise its instructions once. Keep both versions.

## Try Yoodli as a learner
kind: step
time: 15 minutes
do: Each person does **Task 1** with two of the three varieties — for example, a short talk on their paper (research question, method, one finding, one implication) in US and then UK English. Compare the two reports and note one difference. Keep the analysis for your portfolio.

## Before you use either tool
kind: checklist
- No real learner names, voices or work go into either tool without consent
- Age rules checked for the learners who would use the bot
- The bot's instructions forbid asking for personal information
- I read the transcripts and checked what the bot said
- I can name the paper behind each design choice

## Evaluate your bot
kind: questions
- What is your bot's purpose — assessment of, for or as learning — and what evidence from the transcripts shows it served that purpose? Use the table at the top of this page.
- Which of the six design rules did your bot follow, and which did it break?
- What would you change before using it with real learners?
