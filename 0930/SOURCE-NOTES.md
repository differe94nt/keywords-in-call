# 09/30 lesson: editorial and access verification

Checked 29 September 2026. This document records what was inspected; it does not guarantee access from a student's device or account. The student-facing cards link directly to the supporting sources.

## Supplied teaching materials

Both public Drive folder listings and ten Google Docs exports were retrieved. The substantive documents included Learner Analysis, the student and teacher worksheets, both learner-case handouts, the base and profile-specific Say What You See plans, Learning Theory Review and Swain's Comprehensible Output. The Informant document exported as empty text and was not treated as substantive evidence. Slide decks and Forms responses were not used as sources of verified findings.

The lesson retains the profile → evidence → design decision sequence and the informant/guesser activity. It qualifies the handouts in several places:

- Reported preferences are not fixed learning-style types; linguistic output alone does not establish anxiety, disability, motivation or access needs.
- The classroom learner stories are illustrative scenarios, separate from the corpus-based assignment.
- Comprehensible input is a theoretical concept, not a rule that the next CEFR band equals i+1.
- Scaffolding and ZPD have related but distinct origins; scaffolds should respond to performance rather than disappear on a fixed timetable.
- Pushed output and revision create learning opportunities but do not prove acquisition. The original game measures image similarity, not English proficiency.
- A modality alternative must preserve the intended assessment construct; written rehearsal cannot by itself establish a speaking outcome.

## Corpus checks

| Resource | What was verified | What remains untested |
| --- | --- | --- |
| PELIC | Public repository, licence, schema; 20,001-byte range of actual compiled CSV retrieved; 15 headers confirmed; initial learner/text rows inspected. About 174 MB complete file uses Git LFS. | Complete download/import; candidate learner selection across all records. No actual corpus excerpts redistributed. |
| NICT JLE | Full 7 MB v4.1 ZIP downloaded and opened. `LearnerOriginal/file00003.txt` and its annotated counterpart exist; header, `<A>`/`<B>` roles and `crr` correction attributes inspected. | Audio access; no student account needed for the tested ZIP. |
| ICNALE | Official download instructions, password registration, naming conventions, background sheet, module descriptions and no-redistribution terms. | Registration, archive extraction and live query session. |
| SLABank | Current access rules and Vercellotti/PAROLE corpus descriptions, speaker IDs and file conventions. | Registration/email confirmation and authenticated transcripts/media. |
| EFCAMDAT | Current university-account application/approval route and 2023 user agreement. | Approval, files and current release schemas. |
| MERLIN | Languages, licence, metadata and platform instructions. | Download returned anti-bot page in research tool; ANNIS rendered only an application shell. Ordinary browser access may differ. |
| CLC–FCE | Current Cambridge v1.1 page and registration/licence notice, reached from iLexIR. Includes restrictions beyond the older description of a public subset. | Registration and current XML/JSONL files. |
| ICLE | Current official notice reports delayed September 2026 free release; trial linked. | Full/trial retrieval or institutional credentials. |
| LINDSEI | Official CD-ROM/handbook distribution and absence of audio recordings on CD. | Purchase, installation and institution's licence. |
| Guangwai–Lancaster | Official host describes learner Mandarin, with spoken/written data and Sketch Engine link. | Legacy Lancaster URL failed; actual query access/account terms and recoverable individual IDs unverified. |
| English Profile, AntConc, LancsBox | Official reference/tool pages and their roles. | Account-specific English Profile access and desktop installations. These are not interchangeable with learner corpora. |

PELIC's README contains inconsistencies: it describes 14 compiled columns but lists 15, and once describes anon_id as a unique text ID. The actual header and documented separate-table schema establish anon_id as the learner key and answer_id as the text key. The helper validates the fields it uses and makes a personal local analysis copy; it does not download data, infer proficiency or modify the source.

## Product verification

Official pages were checked for Say What You See, Gemini Guided Learning/Canvas, NotebookLM practice features, ChatGPT Study mode, Claude Artifacts and Google Forms. A June 2026 Google announcement supports the optional study-notebooks extension. No claim of independent learning effectiveness is based on a vendor page. Live signed-in tool sessions and campus-account availability were not tested. The lesson supplies ordinary-chat and non-AI alternatives.

## Implementation verification

- Regular and standalone versions checked in Chromium at 1440, 768 and 390 CSS pixels: all five phases render without page overflow or JavaScript exceptions.
- Checked corpus filters, theme toggle, support-level demo, deep-link navigation, skip-link focus, copy-denied fallback and actual worksheet file download.
- Printing expands details and uses text mirrors to preserve long textarea contents.
- Independent code/content review checked all Markdown files, the renderer and the PELIC helper. A skip-link routing defect was corrected.
- Helper synthetic checks: writing-class filter, unique text-ID counts, Unicode/multiline preservation, missing learner, invalid/LFS header and refusal to overwrite an existing file or the source.

The page and sources were prepared locally; this task did not publish or push the site.

## Classroom/homework separation revision

At the instructor’s request, all links to the two Drive folders and their Google Docs were removed from the 09/30 student-facing content, including the sources section and standalone page. The profile-story PDF itself was retrieved and read; its three complete learner stories now appear in flip cards. Reverse sides contain open design questions, not the instructor’s completed plans.

Classroom work now uses the profile stories and learned theories to create one lesson plan. Corpus selection and needs analysis are homework; students can alternatively analyze one speaker in an appropriate public video. Cambridge English’s B1 Preliminary preparation page confirms the Kenza/Mohammed video and examiner comments; IELTS’s official score-resources page supplies speaking clips, transcripts and comments. Embedded playback on student devices remains untested. The guide requires timestamped evidence, checked transcription and a bounded performance analysis.

Flip-card keyboard activation, active-face focus/inert state, mobile layout and absence of Drive/Docs links are checked in both page versions. Printing exposes both card faces and restores their prior accessibility state afterward. Existing worksheet local autosave is preserved and its explanatory text corrected.
