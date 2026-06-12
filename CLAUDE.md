# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **curriculum / course-content repository**, not a software project. It holds the
teaching materials Alexander Booth (the Head Program Instructor) uses to run IBM Data Science
and IBM Data Analyst cohorts: lab notebooks, datasets, lecture transcripts, "Big Ideas" decks,
and authored module summaries.

There is **no build, lint, test, or CI**. "Doing work" here means one of:
- Writing or refining a `Module_NN/README.md` summary for a module.
- Organizing/copying lab notebooks and datasets into the right unit folders.
- Preparing a **Live Session** folder (usually a solved + unsolved version of a lab).
- Standing up a new cohort folder by adapting an existing one.

## Directory taxonomy

```
IBM-<PROGRAM>-<START_DATE>/        cohort, e.g. IBM-IBSC-2026-01-28
  README.md                        cohort overview (module map, prereqs)
  Module_NN/                       Module_00 … Module_10
    README.md                      authored "Big Ideas" module summary (the main maintained artifact)
    Downloads/                     lecture-transcript .txt files (source material for the README)
    N.NN/                          a lesson/unit: notebooks + datasets
    N.NN - Live Session/           live-session copy of labs (+ a .gitkeep placeholder)
    *.pdf                          "Big Ideas" deck + live-session presentation
```

- **Two programs, different module maps.** `IBSC` = IBM Data **Science**; `IBDA` = IBM Data
  **Analyst**. They are not interchangeable: IBDA Modules 2–3 are Excel/Cognos; IBSC Module 1 is
  Data Science Methodology, etc. Always confirm which program a module belongs to before copying
  content between cohorts — the numbering and topics differ.
- **Cohorts are forks in time.** Later cohorts (e.g. `IBM-IBSC-2026-04-08`) are derived from
  earlier ones (`IBM-IBSC-2026-01-28`) and refined. The earliest cohort
  (`IBM-IBSC-2025-10-01`) is flatter and has only a cohort-level README.
- **Unit folder names map to the LMS lesson numbers** (`7.03`, `6.11`). Live-session variants
  appear as `N.NN - Live Session` (or occasionally `N.NN-live-session`).
- `.gitkeep` marks folders reserved for content not yet added.

## The module README is the primary authored artifact

Each `Module_NN/README.md` (in the 2026 cohorts) is a hand-written "Big Ideas" summary by
Alexander Booth, **synthesized from the module's own source material** — not invented. When
asked to create or update one, read these inputs first:

1. `Module_NN/Downloads/*.txt` — verbatim lecture transcripts (the authoritative content).
2. The lab notebooks in each `N.NN/` unit (to describe what each lab actually does + its dataset).
3. The `Module NN – Big Ideas*.pdf` deck and any `Prof's ... Study Guides/` PDFs.

Follow the established format of existing module READMEs (see
`IBM-IBSC-2026-01-28/Module_07/README.md` or `IBM-IBDA-2026-04-01/Module_06/README.md` as
templates): a header block (`**Author:** Alexander Booth`, date, cohort), then `## Overview`,
`## Why This Module Matters`, `## What This Module Covers` (numbered concept sections),
`## Labs and Notebooks` (per-unit, citing the notebook filename and dataset), `## Supporting
Materials`, and `## Key Takeaways`. Match the existing voice: concept-first, bolded key terms,
explains the *why* before the *how*.

If a PDF won't extract to readable text, say so in the README rather than fabricating its
contents (existing READMEs do this for cheat-sheet PDFs).

## Lab notebooks

Notebooks are IBM **Skills Network** labs, identifiable by course-code prefixes:
`PY0101EN-*` (Python), `DV0101EN-*` (Data Viz), `DB0201EN-*` (SQL), `DA0101EN-*` (Data Analysis),
`DS0103EN-*` (Methodology). Treat them as upstream lab material — preserve their structure; don't
"clean up" or refactor them unless asked.

- **Datasets** load either from Skills Network CDN URLs (hardcoded in the notebook) or from local
  files committed alongside the notebook: `.csv`, `.db` (SQLite), `.json`, `.xlsx`, `.xml`.
- Some notebooks target **JupyterLite** (filenames containing `jupyterlite`) and use
  `piplite`/`micropip`; these will not run unmodified in a standard kernel.
- Live-session folders typically contain both a solved and an unsolved (`_Learner` / practice)
  version of the same lab.

## Completing lab exercises (filling in solutions)

Skills Network labs ship with empty placeholder cells — `## Write your code here` or
`# your code goes here`. When completing them:

- **Keep the marker line**; write the solution directly below it in the same cell. Don't delete it.
- **Match the author's voice from Modules 4–8** (the truest reference): minimal, close to the IBM
  solution, brief leading comment, explicit `plt.show()` on plots, f-string `print`s, light styling.
  (Module 9's solutions are more elaborate and are *not* the style to copy.)
- **Comment out `!pip install`** lines (deps live in the kernel) and **replace `!wget`** with a
  portable, idempotent `urllib` download (wget isn't installed on macOS) — edit only that line, not
  the whole cell (imports / `read_csv` often share it).
- Mind the survey data's real shapes: `Age` is text buckets (map to numeric midpoints),
  `YearsCodePro` mixes numbers with `"Less than 1 year"`/`"More than 50 years"`, and the technology
  columns (languages, databases, tools) are `;`-delimited **multi-select** strings (split + explode
  before counting).
- **Execute** with `jupyter nbconvert --to notebook --execute --inplace` so plots embed as outputs
  (run with the inline backend — do NOT set `MPLBACKEND=Agg`, or `plt.show()` produces no image).

## Running things

Notebooks target a conda kernel displayed as **`dev`** (Python 3.10) — the kernelspec is
`{"display_name": "dev", "name": "python3"}`. If it's missing, recreate it:

```bash
conda create -y -n dev python=3.10
conda install -y -n dev pandas numpy matplotlib seaborn scipy scikit-learn requests beautifulsoup4 lxml openpyxl jupyter nbconvert ipykernel
conda run -n dev python -m ipykernel install --user --name dev --display-name dev
jupyter lab            # then select the "dev" kernel
```

- Large capstone datasets (the Stack Overflow survey `.csv` ~160 MB and `.sqlite` ~210 MB) are
  **downloaded at runtime** and git-ignored — never commit them. Small datasets are committed.
- Some notebooks target **JupyterLite** (filenames containing `jupyterlite`) and use
  `piplite`/`micropip`; these will not run unmodified in a standard kernel.
- Dash apps (e.g. `IBM-IBSC-2026-01-28/Module_06/6.12/*.py`): `python "path/to/Dash_wildfire.py"`
  (serves on `http://127.0.0.1:8050`).

## Git conventions

Commit messages are short, lowercase, and tied to teaching milestones rather than code changes —
e.g. `M9 launch`, `ibda 10 init`, `m8 live session`, `live session content`. A "launch" commit
adds a module's materials; a "live session" commit adds that week's session folder. Match this
style. Work happens directly on `main`.
