# Status

## Session 1 (2026-10-30)
- Read `instructions.md` and `background.md`.
- Stage 1 done: proposed structure saved in `structure.md`.
- Added rule to `instructions.md`: ask unclear points via clickable AskUserQuestion options.
- Format: a self-contained slide deck to share (not a talk), so slides must be readable without a presenter.
- Decided: 15–20 slides; audience has used chatbots but not agents; provider-neutral, with VS Code + Claude Code as one example; this project folder is the running example.
- Stage 2 done: all sections agreed, plus additions, drops and design (minimal light blue). Everything recorded in `structure.md`.
- Stage 3 settings: title "Jump-starting AI agents", subtitle "A practical quick start for economists"; Simon Martin, simon.martin@univie.ac.at, https://sites.google.com/view/simonmartinecon/, plus the GitHub repo link; 16:9; title slide shows "Version 0.1, October 2026". LaTeX (MiKTeX) is installed with fontawesome5, tcolorbox, listings, forest and dirtree.
- Stage 3 done: `slides.tex` compiled to `slides.pdf` (18 slides, no overflows). Examples are included from `examples/` (Stata snippet, `\input` snippet, two folder trees); slide 14 includes `instructions.md` itself.
- Added during Stage 3: objective/audience/prerequisites on "About these slides"; slide 5 "What it is, and what it isn't" (token-guessing machine; not a store of truth); closing slide 18 "Get started now" (folder → context files → instructions.md → "Read the instructions.").
- Stata example is runnable (Stata 15 at `C:\Program Files (x86)\Stata15\StataMP-64.exe`, run from `examples/` with `/e do wage_regs.do`). It uses the built-in `nlsw88` data and writes `examples/output/tables/wage_regs.tex`, which test-compiles in a minimal paper.
- Git: branch `main`, commit email simon.martin@univie.ac.at. `.gitignore` excludes `recordings/`, `instr-start.txt` and LaTeX/Stata build files. Public repo: https://github.com/simonmartinecon/jumpstart-ai (remote `origin`), linked via `\repourl`.
- `README.md` is generated from `slides.tex` by `make_readme.py` (run `python make_readme.py` after every change to the slides; never edit `README.md` by hand).
- Final check done (grammar, style, flow, consistency with `background.md`). Fixed: slide 14 cut off at the end; email hyphenated on slide 17; "background files" vs "context files" (now "context files" throughout); outdated folder tree on slide 9; "in euros" → "in percent" (log wages); clearer "what to avoid" on slide 15; example sentences in italics on slide 13; GitHub link in the "Meta" point; gap on slide 5.

- Added: disclaimer at the bottom of the title slide (practical focus; ethics and data policies are up to the reader), also at the top of `README.md`; closing slide 19 "Thanks and further reading" (Anton Korinek, Scott Cunningham, Paul Goldsmith-Pinkham), which now carries the contact box (removed from slide 17). Slide 14 shows an excerpt of `instructions.md` (lines 1–10 and 12–20) with a link to the full file on GitHub; the README shows the same excerpt.

- Added slide 9 "A powerful tool, not a substitute for you" (after "You stay in charge"): powerful if used wisely, sharpens your understanding; but don't make yourself redundant, stay on top of every step as with an RA. Deck is now 20 slides.

- URLs on the thanks slide now shown in full (https://...) via `\link`. `structure.md` now starts with the final 20-slide outline. Language check of the new slides (disclaimer, slide 9, slide 20) done.

## Workflow after each change
1. `latexmk -pdf slides.tex`
2. `python make_readme.py`
3. Commit and push.

## Open TODOs
- Slides 17 ("Putting it together") and 18 ("Get started now") overlap on purpose; merge them if the deck should be shorter.
