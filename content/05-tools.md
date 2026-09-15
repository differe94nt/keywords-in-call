# Step 5 · The tools, and what each one cannot do

The question is not which tool is best. It is whether the tool is **reading a literature index** or **writing from a model's memory**. Only the first kind can be checked by following its links; the second has no links to follow.

Filter by type. The tools the class actually used are marked from the response sheet.

<!--
HOW TO EDIT A TOOL
  ## Tool name
  type:  Grounded search | Chatbot | Discovery map | Citation check | Reference manager
  match: names to look for in the form answers, separated by |
  does:  what it does
  limit: what it cannot do, or does badly
  best:  the job it is actually good for
  link:  https://...
-->

## ChatGPT
type: Chatbot
match: chatgpt | chat gpt | gpt-4 | gpt-5 | openai
does: Writes, rewrites, summarises and explains. With browsing or a file upload it can work from sources you supply.
limit: Without an uploaded file it writes from model memory, so citations may be plausible and non-existent. It rarely says how confident it is, and it smooths disagreement between sources into consensus.
best: Restructuring a summary you wrote, or explaining a method section you have already read.
link: https://chatgpt.com

## Claude
type: Chatbot
match: claude | anthropic
does: Same class of tool as ChatGPT; handles long uploaded PDFs well and holds several papers in view at once.
limit: Still generates citations when none are supplied. Long context does not mean it read carefully — it can still attribute one paper's claim to another.
best: Comparing five PDFs you have uploaded, and asking where they disagree.
link: https://claude.ai

## Gemini
type: Chatbot
match: gemini | bard
does: General assistant, integrated with Google Docs and Drive.
limit: Same fabrication risk when asked for literature it has not been given. Search grounding is inconsistent — sometimes cited, sometimes not.
best: Working over documents already in your Drive folder.
link: https://gemini.google.com

## NotebookLM
type: Grounded search
match: notebooklm | notebook lm | gemini notebook
does: Answers only from the sources you upload, and puts an inline citation on each sentence pointing back to the passage.
limit: It cannot find literature for you — the reading list is your responsibility, and a biased set of five gives a confident, biased summary. Citations point to your PDFs, not to the wider field.
best: Exactly this assignment: five PDFs in, a summary out, with every sentence traceable to a page.
link: https://notebooklm.google.com

## DeepSeek
type: Chatbot
match: deepseek
does: Open-weight assistant with a reasoning mode that shows its working.
limit: Visible reasoning is not verified reasoning; it can walk confidently to a fabricated reference. Coverage of paywalled applied linguistics work is thin.
best: A second opinion on a summary, to see which claims two models both make.
link: https://chat.deepseek.com

## Perplexity
type: Grounded search
match: perplexity
does: Searches the web and answers with numbered links you can open.
limit: It ranks web pages, not peer-reviewed literature, so blogs and publisher marketing pages sit beside journal articles. The link may exist while the sentence it supports is still a paraphrase too far.
best: Finding out whether a claim exists anywhere, then going to a database to confirm it properly.
link: https://www.perplexity.ai

## Scopus AI
type: Grounded search
match: scopus
does: Generates summaries over Scopus-indexed abstracts, with the source records attached.
limit: Only Scopus-indexed work, so it misses unindexed journals and most preprints. Institutional access required, and it summarises abstracts rather than full texts.
best: Checking whether your five studies are representative of the indexed literature or a convenience sample.
link: https://www.scopus.com

## Elicit
type: Grounded search
match: elicit
does: Searches a paper index, then extracts fields into a table — sample, method, outcome, findings — one row per study.
limit: Extraction errors are quiet, especially for sample sizes and effect directions. Coverage leans towards open-access records.
best: Building the first draft of a comparison matrix that you then correct against the PDFs.
link: https://elicit.com

## Consensus
type: Grounded search
match: consensus
does: Returns claim-level answers to a yes/no research question, with the supporting papers listed.
limit: It reports what papers claim, not how well they show it. Its agreement meter reflects the sample it retrieved, not the field.
best: Finding out quickly whether a question is contested before you commit to it.
link: https://consensus.app

## Semantic Scholar
type: Citation check
match: semantic scholar | semanticscholar
does: Free index of about two hundred million papers, with citation contexts showing how later work uses a paper.
limit: Automatically extracted metadata carries occasional errors. Its summaries are short and do not replace reading.
best: Confirming a citation exists, then seeing who cited it and whether they agreed.
link: https://www.semanticscholar.org

## Connected Papers
type: Discovery map
match: connected papers | connectedpapers
does: Builds a similarity graph around one seed paper so you can see its neighbourhood.
limit: Similarity, not influence — a prominent paper can sit at the edge. One seed paper decides the whole map.
best: Checking whether your five studies cluster in one corner of the field.
link: https://www.connectedpapers.com

## Research Rabbit
type: Discovery map
match: research rabbit | researchrabbit
does: Follows citation chains forward and backward from a starting set, and alerts you to new work.
limit: Recommendations inherit the bias of your starting set. Metadata comes from the same open indexes and repeats their gaps.
best: Finding the landmark study your five papers all cite but none of you read.
link: https://www.researchrabbit.ai

## Scite
type: Citation check
match: scite
does: Shows whether citing papers support, contrast or merely mention a claim, and flags retractions.
limit: Classification is automated and imperfect. Full features need a subscription.
best: The last check before you cite something central to your argument.
link: https://scite.ai

## Zotero
type: Reference manager
match: zotero | mendeley | endnote
does: Stores references and PDFs, retrieves metadata by DOI, and formats citations in APA.
limit: It stores whatever you feed it, including a wrong year. It checks nothing for you.
best: Keeping the verified version of every reference, so you never re-type one from a chatbot.
link: https://www.zotero.org
