# Turn evidence into a learning activity

**Choose the learning action first; choose one tool second.** A more advanced tool is useful when it provides something your learner needs: contingent hints, an information gap, source-linked practice, accessible input or feedback on a revision. A polished output is not evidence of learning.

The activities below are teaching proposals. Vendor documentation confirms features, not effectiveness for your selected learner. Account permissions, usage limits and school policies can affect availability; keep a paper or ordinary-chat version ready.

## Say What You See · our shared demonstration
kind: demo
text: The Google Arts & Culture experiment asks users to describe generated images and compares a new generated image with the target. Its visual-match threshold is a game score, not a measure of English proficiency. The landing page and description were checked; completing the embedded game was not tested.
source: [Open Say What You See](https://artsandculture.google.com/experiment/say-what-you-see/jwG3m7wQShZngw?hl=en) · [Google’s description](https://artsandculture.google.com/experiment/say-what-you-see/jwG3m7wQShZngw?hl=en)
- **Model · 2 minutes:** Describe a teacher-selected image aloud: name the objects, add a relationship, then give a justified inference. Identify which wording makes the message precise.
- **Information gap · 4 minutes:** Informant sees the target; guesser sees three alternatives. Describe without showing the target. The guesser asks one clarification question and chooses an image. This adapts the roles in our second Drive folder.
- **Differentiate · 3 minutes:** Offer a word bank or frame where evidence supports it. For greater challenge, change the audience or require a more precise relationship. The goal stays clear communication.
- **Revise and check · 3 minutes:** Improve one ambiguous sentence, explain why, then describe a new image with less help. Record listener success and the target language feature separately from the game score.
- **Fallback:** Use teacher-owned or permitted images on paper or slides. A partner can supply the feedback; an AI account is not necessary for the information gap.

## Gemini · Guided Learning and Canvas
kind: tool
label: Guided practice / interactive drafting
text: Guided Learning supports a tutoring dialogue; Canvas can create or edit documents, code and learning resources. Use a Google account with the feature enabled. School-account controls may differ.
action: Ask for one question at a time, a hint after the learner’s attempt and a new transfer item. For Canvas, request a small interactive practice task with visible answers for teacher review; test its feedback before using it.
limit: An adaptive response is not a validated diagnosis. Check factual accuracy, task difficulty and whether the learner still produces the target language. If the named mode is unavailable, use the same prompt in ordinary chat.
source: [Guided Learning help](https://support.google.com/gemini/answer/16448384?hl=en) · [Canvas help](https://support.google.com/gemini/answer/16047321?hl=en)

## NotebookLM · Source-linked practice
kind: tool
label: Curated sources / retrieval practice
text: NotebookLM offers flashcards and quizzes based on selected sources, with explanations linked back to source material. It requires an eligible Google account; availability and limits vary.
action: Add a teacher-authored mini-lesson and model examples you may upload. Generate five questions focused on one observed need. Check every key and citation, then use one new item after the supported practice.
limit: Uploading a corpus is not necessary. Use your own summary of the learner’s needs and permitted instructional sources. A source citation does not guarantee a good question or a correct interpretation.
source: [Google’s student-feature guide](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-student-features/)

## ChatGPT · Study mode
kind: tool
label: Hints / explanation / revision
text: Open Study mode in a signed-in regular chat. Official documentation lists it across ChatGPT plans; menus and available tools can vary.
action: Give a de-identified needs summary, one goal and success criteria. Ask the tutor to wait for an attempt, offer graduated hints, then require the learner to explain a revision and try a new example.
limit: Study mode can still give direct answers or make mistakes. Review the interaction and the learner’s independent work. Do not treat a chatbot’s claimed CEFR level as an assessment result.
source: [Current Study mode instructions](https://help.openai.com/en/articles/11780217-using-study-mode-in-chatgpt)

## Claude · An interactive practice artifact
kind: tool
label: Branching hints / teacher-controlled feedback
text: Artifacts can contain an interactive tool alongside the chat. Creation is available across Claude plans; templates, sharing and AI-powered interactions have separate plan and access conditions.
action: Ask Claude to build a three-item activity from teacher-written examples, with a hint button, an explanation after submission and a final item without hints. Specify keyboard access, readable text and no data collection. Try correct, incorrect and blank answers yourself.
limit: Generated code and answer keys need testing. Start with a static activity that uses no live model calls. If the artifact is unavailable, request the same activity as a printable table.
source: [Artifacts documentation](https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them) · [Sharing conditions](https://support.claude.com/en/articles/9547008-share-artifacts)

## Gemini study notebooks · a recent extension
kind: tool
label: Announced June 2026 · optional exploration
text: Google describes study notebooks that use uploaded materials, diagnostic quizzes, short lessons and a progress dashboard. This is a product description; access in your course account was not tested.
action: If available, use a teacher-authored lesson and compare the system’s suggested “focus area” with your own evidence-based priority. Save an example where the suggested next step fits or needs correction.
limit: The dashboard is a hypothesis about performance in its tasks, not an independent language-proficiency measure. Keep this an optional extension; the assignment does not depend on access.
source: [Google’s June 2026 announcement](https://blog.google/innovation-and-ai/products/gemini-app/gemini-study-notebooks/)

## Google Forms + Docs · a practical baseline
kind: tool
label: Transparent feedback / low complexity
text: Use a teacher-written Forms quiz for a short check and Docs comments for revision. A teacher-managed form needs account setup; student sign-in depends on its settings. Do not assume the historical forms in Drive are the submission destination for this week.
action: Make three items tied to the learning goal, explain each answer and ask for one new sentence in Docs or on paper. Compare this workflow with the advanced tool: what additional learner action does the AI version make possible?
limit: A form score describes the items attempted. Use a new item and, if studying retention later, a delayed check. Test form access in a signed-out browser before class.
source: [Create quizzes in Google Forms](https://support.google.com/docs/answer/7032287?hl=en)

## Prompt 1 · Audit the evidence before designing
kind: prompt
purpose: Use your own de-identified analytic notes; include corpus text only where its terms permit.
prompt: Act as a cautious language-teaching assistant. I will provide a corpus name, anonymous learner/script ID, task context and my observations. Separate your response into (1) observed evidence, (2) plausible interpretation with uncertainty, and (3) unknown information to ask the learner. Cite my sample/line IDs for each observation. Identify one strength and at most two instructional priorities. Do not invent quotations, scores, goals, anxiety, disability, learning styles or CEFR levels. Do not attribute errors to L1 without supporting evidence. If my notes do not support a conclusion, say so. Here are my notes: [paste permitted notes].

## Prompt 2 · Design support that can fade
kind: prompt
purpose: Works in ordinary ChatGPT, Gemini or Claude chat; special paid features are not required.
prompt: Design a 12-minute language activity for this provisional learner profile: [profile]. Observed priority: [evidence + sample IDs]. Learning goal: [observable goal]. Context and constraints: [confirmed facts; label assumptions]. Use [chosen tool, or paper]. Give a brief model, guided practice with one targeted scaffold, feedback requiring learner revision, and a new less-supported transfer task. State exactly when to reduce or restore support. Keep the same core learning goal across versions. Provide learner-facing instructions, teacher notes, an answer key where appropriate and a three-item success checklist. Explain the mechanism using one relevant learning concept; do not invent citations or claim guaranteed learning. Include a low-bandwidth alternative. Label all examples you create as synthetic.

## Prompt 3 · Build an interactive activity
kind: prompt
purpose: Try in Claude Artifacts or Gemini Canvas after approving the activity content.
prompt: Build a small self-contained interactive language activity from the teacher-approved content below. Use three practice items, optional graduated hints and one new final item without hints. Let learners attempt before showing feedback; explain answers without grading personality or assigning a CEFR level. Include a teacher answer-key view. Use large readable text, keyboard-operable controls and explicit labels; do not rely on colour alone. Use no external APIs, trackers or collection of learner data. Make a printable alternative. Test correct, incorrect and empty answers and list any limitations. Do not rewrite the learning goal. Approved content: [paste your own activity and key].

## Prompt 4 · Challenge the plan
kind: prompt
purpose: Use after generating; the teacher still checks the response.
prompt: Audit the following activity against this learner evidence and goal: [paste your own summary and plan]. For each design choice, identify the evidence that supports it, any unsupported assumption, and a feasible improvement. Check that the learner must use the target language, the scaffold addresses the observed need, and the independent check uses new content. Distinguish usability, immediate task performance and longer-term learning. Do not treat a game score, attractive output or learner enjoyment as proof of learning. Return the three most important revisions only.
