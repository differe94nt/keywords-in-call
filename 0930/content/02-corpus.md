# Find one learner, then build a defensible profile

**Choose one corpus, not the whole list.** PELIC is the default for English writing; NICT JLE is the small-download alternative for spoken-language transcripts. Arrange registrations before class for other routes. If a dataset provides only one script or interview, use two passages from different parts and describe the narrower evidence base.

**Access checked 29 September 2026.** Public, free of charge and licence-free are different claims. The cards distinguish a verified download from a documented access procedure. No authenticated applications were completed. Keep restricted corpus data within the access conditions; use your own analytic summaries in AI prompts unless the terms permit uploading the text.

## PELIC · English writing
kind: corpus
status: ready
badge: Public download · large file
access: No account required. CC BY-NC-ND 4.0 applies. The compiled CSV is about 174 MB; its real header and first rows were retrieved. A complete archive import was not tested.
profile: Longitudinal data with stable learner `anon_id` and text `answer_id`. The compiled file includes L1, semester, course level, task ID and text; goals, anxiety and accessibility needs are not established by those fields.
route: Open `PELIC_compiled.csv` → **Download raw file** (the button on GitHub's file page), or use the [direct data link](https://media.githubusercontent.com/media/ELI-Data-Mining-Group/PELIC-dataset/master/PELIC_compiled.csv) — 182 MB, so start it before you need it. Use Excel or the optional local extractor below; import the small result into Sheets if desired. Filter one `anon_id`, preferably with two or three writing texts (`class_id` = `w`). Look up `question_id` in `corpus_files/question.csv` for the prompt. Record `version`, `semester`, `level_id` and `answer_id`; do not treat revised versions as separate learners.
caution: A Git LFS pointer is not the dataset. Copying the `raw.githubusercontent.com` address gives a three-line pointer file, not data — verified. Use the Download raw file button or the direct data link above. Check for the CSV header beginning `answer_id,anon_id`. `anon_id` identifies a learner, not a unique text; the README has a wording error here. Keep original data intact and follow the licence when sharing or adapting it.
source: [Repository, schema and licence](https://github.com/ELI-Data-Mining-Group/PELIC-dataset) · [Direct data link, 182 MB](https://media.githubusercontent.com/media/ELI-Data-Mining-Group/PELIC-dataset/master/PELIC_compiled.csv) · [Compiled CSV](https://github.com/ELI-Data-Mining-Group/PELIC-dataset/blob/master/PELIC_compiled.csv) · [Task prompts](https://github.com/ELI-Data-Mining-Group/PELIC-dataset/blob/master/corpus_files/question.csv)

## NICT JLE · English interview transcripts
kind: corpus
status: ready
badge: Public download · verified ZIP
access: The 7 MB v4.1 ZIP downloaded and opened successfully. No registration; CC BY-SA 3.0. It contains 1,281 learner interview transcripts; 167 also have error-tagged versions. The same interview in two folders is not two samples.
profile: Japanese learners of English, with nine SST levels. Use the filename as an interview identifier. Supplied headers include task labels and available background/test fields; blank fields remain unknown. These are not CEFR levels.
route: Open the official page → Sample and Tag List → Download. Unzip and choose `LearnerOriginal/file00003.txt`, for example. Inspect its header and two task sections. The corresponding annotated file is `LearnerErrortagged/E_file00003.txt`. Analyze only `<B>` learner turns; use `<A>` interviewer turns for context, not learner counts.
caution: Keep a raw copy. Annotation attributes such as `crr` contain corrections; do not count them as learner output. Filled pauses, restarts and repair require explicit counting rules. The transcript download does not establish access to audio, so do not infer pronunciation or speaking rate from it.
source: [Official page, sample, tag list, licence and download](https://alaginrc.nict.go.jp/nict_jle/index_E.html)

## ICNALE · English across Asian contexts
kind: corpus
status: register
badge: Register before class
access: Free access is conditional: registration supplies the password for downloaded archives. The public query interface lacks learner attributes and is not kept current. Registration and archive extraction were not tested.
profile: Written Essays provides two topics per participant, with proficiency bands and a background sheet. Use module + region + participant ID together; the two topics are not automatically longitudinal evidence.
route: Register through Download → obtain the password → download Written Essays v2.6 and the Participant Background Survey Sheet. Select an individual file, then match its region/participant ID to the sheet and its second topic. The documented filename pattern includes module, region, task, ID and proficiency (for example `WE_CHN_PTJ0_001_B1_1`). Taiwan is among the represented contexts.
caution: The official terms prohibit reproducing or redistributing any part or whole. Do not place texts in a public assignment, shared handout or external AI tool without permission. Use file references and your own analysis where excerpts cannot be shared. Edited Essays contains professional revisions, not evidence of later learner improvement.
source: [Download and naming guide](https://language.sakura.ne.jp/icnale/download.html) · [Modules](https://language.sakura.ne.jp/icnale/modules.html) · [Terms](https://language.sakura.ne.jp/icnale/index.html)

## SLABank · Select a named subcorpus
kind: corpus
status: register
badge: Account and email confirmation
access: Official SLABank access instructions require registration and email confirmation. Descriptions are public; authenticated transcripts and media were not tested. Collection terms and citation requirements apply.
profile: For repeated English speech, choose Vercellotti: the first four filename digits identify an anonymous speaker. PAROLE is an alternative with subject profiles and task-linked IDs. SLABank as a whole contains different languages and designs.
route: Open TalkBank SLABank → Login/register → Index to Corpora → English–Vercellotti → Browsable transcripts. Select two files with the same four-digit speaker ID; record topic and session. In CHAT, identify the learner’s speaker code from the header and retain only that speaker’s main tiers for counts.
caution: Exclude interviewer turns and dependent annotation tiers; do not simply count every word in a .cha file. Topics differ across monologues. Use audio for claims about pronunciation or temporal fluency only when it is actually available to you.
source: [SLABank access](https://talkbank.org/slabank/access.html) · [Vercellotti IDs and collection](https://talkbank.org/slabank/access/English/Vercellotti.html) · [PAROLE](https://talkbank.org/slabank/access/English/PAROLE.html) · [Ground rules](https://talkbank.org/0share/rules.html)

## EFCAMDAT · English writing over courses
kind: corpus
status: advance
badge: Academic application and approval
access: Current instructions require academic affiliation, university email authenticated with Google, and administrator approval before Drive access. The landing page and user agreement were checked; approval and data download were not tested.
profile: Large-scale English writing across course levels, potentially multiple texts per learner. The approved release’s documentation must establish its learner ID, task and date fields before selection.
route: Apply before class. Once approved, use the documented cleaned XLSX or XML release; filter one learner and compare tasks while retaining level and timing. Do not rely on old tutorials describing a different interface.
caution: Not a dependable next-day access route. The agreement permits brief credited teaching extracts with a non-responsibility declaration, but broader sharing requires consent. See the agreement before distributing files.
source: [Current access procedure](https://ef-lab.mmll.cam.ac.uk/EFCAMDAT.html) · [User agreement, §§2.1–2.3](https://ef-lab.mmll.cam.ac.uk/assets/pdf/EFCamDat-User-Agreement-2023.pdf)

## MERLIN · German, Italian and Czech
kind: corpus
status: check
badge: Open licence · browser check needed
access: CC BY-SA 4.0. The platform and access instructions were reachable; the linked repository returned an anti-bot page and ANNIS only an application shell in this check. Student-browser download/query remains unverified.
profile: CEFR-rated written texts with error annotations and target hypotheses. This is not English learner data. Metadata describe the author and task; repeated longitudinal learner IDs were not verified.
route: Try the platform’s TXT download or ANNIS → select a language in Corpus List → document icon → Full text → metadata. Distinguish the original text from target hypotheses and the test level from the separately rerated level.
caution: Use for a non-English project or a multilingual rating demonstration. Have a working text ready before class; a single text supports a performance profile, not a complete learner trajectory.
source: [Platform and instructions](https://www.merlin-platform.eu/) · [Corpus metadata](https://www.merlin-platform.eu/C_mcorpus.php) · [Repository](https://clarin.eurac.edu/repository/xmlui/handle/20.500.12124/59)

## CLC–FCE · English exam writing
kind: corpus
status: advance
badge: Registration and specific terms
access: The current official release is v1.1 (2026), reached from iLexIR. A registration form, intended use and licence agreement are required. The page was checked; post-registration downloads were not tested.
profile: 1,244 scripts with scores, errors and background information. Use the supplied script ID and its tasks; do not assume it links different exam sittings or reflects all language skills.
route: Follow the Cambridge dataset page → review the licence → register. In the authorized XML/JSONL files, keep learner text separate from prompts, corrections and metadata. Use the release documentation for fields and score interpretation.
caution: The current page forbids corpus redistribution and adds approval requirements for releasing derived items, including statistics. It permits excerpts under 100 words. Keep coursework private within permitted use or obtain clarification before public release. Do not assume older copies carry identical terms.
source: [Current dataset and licence](https://researchdatasets.cambridge.org/datasets/clc-fce-dataset) · [iLexIR link](https://ilexir.co.uk/datasets/index.html)

## ICLE and LINDSEI · Arrange access first
kind: corpus
status: advance
badge: Not an immediate open-data route
access: ICLE’s official notice says its planned 15 September 2026 free release is delayed; a 100-text trial is linked. LINDSEI’s official distribution is a CD-ROM/handbook order. Do not promise free full access for this class.
profile: ICLE contains English learner essays; LINDSEI contains English learner interviews. Use the sample/participant documentation supplied with the version you can access.
route: Check institutional access or the ICLE trial before selecting a learner. For LINDSEI, ensure the licensed data and software are usable on your computer; its CD-ROM does not include the sound recordings.
caution: Use as advance-access alternatives. If access is unresolved, select PELIC or NICT JLE for this assignment.
source: [ICLE current notice](https://uclouvain.be/en/research-institutes/ilc/cecl/icle) · [LINDSEI distribution](https://uclouvain.be/en/research-institutes/ilc/cecl/lindsei-cd-rom-and-handbook)

## Guangwai–Lancaster · Mandarin as an L2
kind: corpus
status: check
badge: Non-English · query access unverified
access: The official host describes the corpus and links to Sketch Engine. The supplied Lancaster legacy URL failed in this check; the querying session, account conditions and individual metadata could not be verified.
profile: Spoken and written learner Mandarin Chinese with error annotation. Appropriate for a Chinese-as-L2 project, not evidence about English performance.
route: Use the official host’s corpus link; confirm account access and recoverable individual IDs before committing to this route. Record the available metadata and annotation layer.
caution: If you cannot retrieve an individual learner sample and its context, choose another corpus. Corpus-wide frequencies cannot stand in for an individual profile.
source: [Official host description](https://www.sketchengine.eu/guangwai-lancaster-chinese-learner-corpus/)

## 1 · Select and document
kind: workflow
text: Choose one anonymous learner, or one script/interview if that is all the data identify. Aim for two short samples from the same learner; record corpus/version, ID, task, date/level if supplied, and access terms. State when samples come from one sitting.

## 2 · Read before counting
kind: workflow
text: Read the task and the original learner response. Record one communicative strength first. Keep prompts, interviewer words, target corrections and annotation tags out of learner counts. Keep the original unchanged and document every exclusion in an analysis copy.

## 3 · Investigate two patterns
kind: workflow
text: Choose features relevant to the task: tense in a past narrative, referents in a description, collocation, connectors, repair or register. Mark successful uses as well as difficulty. Use word search or a concordancer to find examples, then inspect each in context.

## 4 · Make counts interpretable
kind: workflow
text: Report the denominator: “3 mismatches in 8 obligatory past-tense contexts,” not just “3 errors.” For frequencies across unequal texts, use occurrences ÷ learner-word count × 100, with the same tokenization rule. Do not rank vocabulary ability using raw type–token ratios from unequal, tiny samples.

## 5 · Form a provisional profile
kind: workflow
text: Separate observed evidence, interpretation and unknowns. Two texts can suggest an instructional priority; they cannot establish a cause, diagnose anxiety or assign a global CEFR level. L1 or group averages do not justify attributing an individual’s difficulty to transfer.

## 6 · Design, then check transfer
kind: workflow
text: Turn one priority into a measurable goal. Design guided practice plus a less-supported task using new content. Decide what success would look like and what result would make you revise the profile. A corpus-based proposal is not a claim that the learner has tried your activity.

## Concordancers and reference tools
kind: resource
text: A corpus is the evidence; software helps inspect it. For a few passages, a spreadsheet and close reading are enough. Use a concordancer when there is enough text to justify it.
- **AntConc:** save learner-only UTF-8 .txt files, one per sample → open them as a corpus → search a target in the concordance/KWIC view → inspect surrounding text and record useful instances. Confirm the interface for your installed version. [Download and manuals](https://www.laurenceanthony.net/software/antconc/).
- **LancsBox:** import learner-only text files into a new corpus → use KWIC/Words to inspect patterns → check context before interpreting frequencies. Free for noncommercial use under its licence; installation was not tested. [Official site](https://lancsbox.lancs.ac.uk/).
- **English Profile:** use the grammar/vocabulary reference profiles to contextualize a target feature. They are not an individual learner corpus or a diagnostic CEFR test. [English Profile](https://www.englishprofile.org/).
- **Need another corpus?** Use the [UCLouvain learner-corpus directory](https://uclouvain.be/en/research-institutes/ilc/cecl/learner-corpora-around-the-world.html), then check the selected corpus’s own access terms and metadata.
