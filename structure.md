# Structure

## Final deck as built (21 slides, version 0.1)
Introduction
1. Title (with disclaimer: practical focus; ethics, data policies and copyright are out of scope, check your institution's, journals' and funders' rules)
2. About these slides (objective, audience, prerequisites, caveat, contact)
3. Chatbot vs agent
4. "Coding agent": not just for coding (misconceptions + example tasks)
5. The model behind the agent: what it is, and isn't (LLM vs agent; token-guessing machine; not a store of truth)
6. What you need (subscription, software, setup; settings)

Mindset
7. The basic mindset (overview of three ideas)
8. Your agent is your research assistant
9. You stay in charge
10. A powerful tool, not a substitute for you
11. Project = folder

Practical rules
12. Plain text for everything you work on
13. No copy/paste
14. Script everything (Stata example + do/don't)

instructions.md
15. `instructions.md`: the contract
16. Example: the `instructions.md` behind these slides (excerpt + GitHub link)

Ways of working
17. Ways of working (asynchronous; sparring partner)
18. Pitfalls (citations, backups, confidential data)

Jump start
19. Putting it together: the jump start
20. Get started now
21. Thanks and further reading

The sections below document the planning in Stages 1 and 2.

# Proposed structure (Stage 1, draft for deliberation)

Decisions so far: a self-contained slide deck to share (not a talk); 15–20 slides; audience has used chatbots but not agents; principles provider-neutral, with VS Code + Claude Code as one example setup; this project folder serves as the running example.

## Agreed layout for sections 0–3 (Stage 2)
- 0 → title slide + short "About these slides" slide: objective (get started on one of your own projects right after skimming the slides), audience (economists in academia, but widely applicable), prerequisites (almost none; a ~20 USD/month subscription with any provider), personal take, adjust to your setup, contact.
- 1 → one slide: two-column chatbot vs agent table (files, context, copy/paste, planning), bottom line: basics = 90–95% of gains, skip hype features.
- 2 → one slide: the two misconceptions, then short example tasks for writing, admin, theory, empirics.
- 2b (added in Stage 3) → one slide "What it is, and what it isn't": "just a token-guessing machine?" (technically yes, but it can follow arguments, plan and check proofs; judge by results) vs "not a store of truth" (not a database or Wikipedia; reconstructs facts, so they can be wrong, outdated or invented). Key box: provide sources, compute in code. Deck is now 17 slides.
- 3 → one slide, two columns: left = subscription, software, setup help; right = settings (any model, medium effort, what eats tokens). Token usage therefore moves here from section 7.

## Agreed layout for sections 5–8 (Stage 2)
- 5 → two slides: (a) typical sections + "format barely matters" + "why bother: 10–15 min"; (b) this project's real `instructions.md`, included from file.
- 6 → one slide, two columns: asynchronous (left) and sparring partner (right), each with one sample prompt.
- 7 → one slide: citations (exact rule wording), backups and safety, data confidentiality.
- 8 → one slide: 5 numbered steps + 2–3 sample first prompts.
- Total: 16 slides.

## 0. Title and caveat
- My personal take in a very fast-moving field; it works for me, adjust it to your setup; happy to discuss any time.

## 1. Why this matters
- Chatbot vs agent: copy/paste, short-lived context vs reads/writes your files, keeps the whole context, plans its own subtasks.
- The basics get you ~90–95% of the gains; ignore the hype features (skills, GitHub integration, ...) for now.

## 2. Two misconceptions about "coding agents"
- Almost everything you do on a computer is "coding": writing, formatting, reading, calculating, cross-referencing.
- Not only for empirical work: admin, writing and theory too (checking a proposition; turning notes into a formal proposition, with a sample from your field).

## 3. What you need
- A ~20 USD/month subscription from any provider (free tiers too limited; no need for 200 USD).
- An editor plus an agent (e.g. VS Code + Claude Code).
- Settings: any current model, medium effort; high only for thorough checks.

## 4. Core mindset
**Agreed layout (Stage 2):**
- 4.1 → two slides: (a) your job: context, instructions, how to handle unclear points, with two example phrasings ("NEVER make assumptions..." / "leave a TODO..."); (b) you stay in charge: mistakes, memory drift, verification, AI slop.
- 4.2 → two folder trees side by side: a typical research paper and this slides project.
- 4.3 → two-column format table (plain text = work on; binary = input/output only), XLSX vs CSV example, "try it" tip (open a .docx/.pdf in Notepad), one line on change tracking.
- 4.4 and 4.5 → separate slides; 4.5 gets a short Stata (esttab) snippet writing a `.tex` table plus the `\input{}` line, and a do/don't table of prompts.

Original draft:
- 4.1 The agent is your RA: very capable given context. You supply background, terminology, expected output, how to handle unclear points. It makes mistakes; you stay responsible: verify, leave time for it (AI slop shows). Memory drifts as context grows: ask it to re-read / double-check now and then.
- 4.2 Project = folder: literature, data, code, samples, instructions, status.
- 4.3 Plain text for anything you work on; binary only for pure input and final output. Faster, cheaper in tokens, easy to track over time.
- 4.4 No copy/paste: point the agent to a file or line; have it write straight into the final document.
- 4.5 Script everything: code produces the final tables (`.tex` via `\input`); ask the agent to change the code, not the output; calculations go into code, not the chat.

## 5. `instructions.md`: the contract
- Typical sections: scope, literature, stages, main output, software, style sample, checks, logging (`status.md`).
- Format barely matters (.md or .txt, no syntax rules); a little structure helps.
- Why bother: 10–15 minutes of writing forces clear thinking.
- Citation rule: cite only from `/literature`.

## 6. Ways of working
- Asynchronous: settle decisions up front (or defer as TODOs), run several agents in parallel, reconcile afterwards.
- Sparring partner: test ideas against your paper and the literature before taking them to colleagues.

## 7. Practical pitfalls
- Made-up citations (the `/literature` rule).
- Token usage: parallel web searches and binary files are what eat tokens.

## 8. Putting it together: the 5-minute jump start
- Folder → background files → `instructions.md` → open the agent → "read the instructions" → go.

## Agreed additions (Stage 2)
- Backups and safety (Dropbox/OneDrive history; read permission prompts before approving) → section 7.
- Data confidentiality (one line: check licences and institution rules) → section 7.
- Fresh sessions + `status.md` instead of one endless chat → slide 4.1(b), next to memory drift.
- Let the agent set things up (install/explain LaTeX, Stata etc.; convert existing .docx/.pdf drafts to .tex/.md once) → section 3.
- Dropped: co-authors on Word.

## Agreed drops/merges and design (Stage 2)
- Drop grep/awk/sed; "every operation can be scripted, the agent does it for you" goes on the script-everything slide.
- Version control: one sub-bullet on change tracking under plain text.
- Fallibility merged into 4.1(b).
- Design: minimal light blue: white background, light blue frame titles with a thin rule, no navigation symbols, slide numbers bottom right, a few FontAwesome icons, light blue boxes for prompts/examples.

## Candidates for Stage 2 (original list, now resolved above)
- Additions: backups and safety (Dropbox history, permission prompts); data confidentiality (one line); let the agent install/explain software and convert existing .docx/.pdf once; co-authors on Word; fresh sessions + `status.md` instead of one endless chat.
- Examples: folder tree (this project); real `instructions.md` (this project); R/Stata snippet writing a `.tex` table + `\input{}`; 2–3 sample first prompts.
- Drop/merge: drop the grep/awk/sed TODO (merge "everything can be scripted" into 4.5); version control as one sub-bullet under plain text; model/effort/tokens on one "settings" slide.
