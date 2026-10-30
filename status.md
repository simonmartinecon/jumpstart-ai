# Status

## Session 1 (2026-10-30)
- Read `instructions.md` and `background.md`.
- Stage 1 done: proposed structure saved in `structure.md`.
- Added rule to `instructions.md`: ask unclear points via clickable AskUserQuestion options.
- Format: a self-contained slide deck to share (not a talk), so slides must be readable without a presenter.
- Decided: 15–20 slides; audience has used chatbots but not agents; provider-neutral, with VS Code + Claude Code as one example; this project folder is the running example.
- Stage 2 done: all sections agreed, plus additions, drops and design (minimal light blue). Everything recorded in `structure.md`.
- Stage 3 settings: title "Jump-starting AI agents", subtitle "A practical quick start for economists"; Simon Martin, simon.martin@univie.ac.at, https://sites.google.com/view/simonmartinecon/, plus a link to the GitHub repo for these slides; 16:9; title slide shows "Version 0.1, October 2026". LaTeX (MiKTeX) is installed with fontawesome5, tcolorbox, listings, forest and dirtree.
- Stage 3 first draft done: `slides.tex` compiled to `slides.pdf` (17 slides, no overflows). Examples are included from `examples/` (Stata snippet, `\input` snippet, two folder trees); slide 14 includes `instructions.md` itself.
- Changes during Stage 3: "About these slides" now states objective, audience (academic economists, widely applicable) and prerequisites (a ~20 USD plan); new slide 5 "What it is, and what it isn't" (token-guessing machine; not a store of truth).

- Stata example made runnable (Stata 15 at `C:\Program Files (x86)\Stata15\StataMP-64.exe`, run from `examples/` with `/e do wage_regs.do`). It uses the built-in `nlsw88` data and writes `examples/output/tables/wage_regs.tex`, which test-compiles in a minimal paper.
- Git initialised locally (branch `main`, commit email simon.martin@univie.ac.at). `.gitignore` excludes `recordings/`, `instr-start.txt` and LaTeX/Stata build files. Public GitHub repo: https://github.com/simonmartinecon/jumpstart-ai (remote `origin`), linked on the title slide via `\repourl`.

## Next
- Review the first draft with Simon, then do the final checks (grammar, language, style, consistency with `background.md`).

## Open TODOs
- Slide 14 (`instructions.md` in full) uses very small type; consider showing an excerpt instead.
- Small extra gap under the left heading on slide 5.
