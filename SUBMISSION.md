# Practicum 3 Submission

Operating system: Windows
Terminal used: PowerShell and Git Bash
Codex tool used: Codex desktop app
GitHub repository URL: https://github.com/khloudalzubi/insy7970-sprint-practicum

## Setup notes

- Project folder path from `pwd`: `/c/Users/kha0010/insy7970-sprint-practicum`
- `uv run main.py` worked at the starting point and displayed: `Hello from insy7970-sprint-practicum!`
- `uv init` created the starting Python scaffold, including `pyproject.toml`, `.python-version`, `main.py`, `README.md`, and `.gitignore`.
- Confirmed `.gitignore` excludes `.venv/`, `__pycache__/`, `.pytest_cache/`, and `.ruff_cache/`.

## Sprint 1 summary

Codex prompt used before editing `sprint1.md`: "Read docs/specs/sprint1.md. Help me expand this into a complete sprint spec with plan, tasks, out of scope items, and a definition of done. Do not edit code yet."

I defined the Sprint 1 user requirements around the smallest useful CSV inspection workflow: provide a file path, see the row count, read basic run instructions, view column names, and preview the first rows. I kept the requirements WHAT-oriented so they describe user-visible behavior rather than Python implementation details.

One helpful addition from Codex was making the Definition of Done include both successful output and error handling for missing or invalid paths. That made the sprint feel more verifiable instead of just descriptive.

I started with `bat main.py` `bat README.md` and then I ran the Sprint 1 implementation with `uv run main.py data/datatest.csv`. The run succeeded and reported 262 rows, 19 columns, and a preview of the first five data rows. I also checked the error path with `uv run main.py data/missing.csv`, which returned `Error: file not found: data\missing.csv`.

One file I inspected was `data/datatest.csv`. I looked at the header row and the first few records so I could compare the reported column names and preview output against the actual CSV contents.

The Sprint 1 definition of done was met. The tool runs from the command line with the provided CSV path, prints the row count, shows the column names, and displays a short preview. I confirmed the row count by comparing the program output with the CSV line count: the file has one header row plus 262 data rows. I also confirmed the README includes the basic run command and that missing or omitted paths produce clear error or usage messages.

While Codex implemented Sprint 1, I was able to follow the work because it first read the existing documents, then edited `main.py` and `README.md`, and then ran the verification commands from the sprint spec. I had to approve several times for reading, writing, and running `uv`, but I did not need to stop or redirect the implementation.

Sprint 1 commit: `Implement sprint 1`

## Sprint 2 summary

Sprint 2 theme: missing-value summary.

Codex prompt used before editing `sprint2.md`: "I have updated docs/specs/sprint2.md with a Sprint 2 problem statement and 5 user requirements. Follow this loop: review/edit if needed -> implement -> inspect -> run/check. Making sure Sprint 2 tests both the new behavior and the Sprint 1 behavior that should still work."

For Sprint 2, I chose the missing-value summary theme because the provided CSV has realistic blank fields and this was a natural extension of the basic inspection tool. I updated `docs/specs/sprint2.md` with requirements for missing counts, missing percentages, whitespace-only missing values, highest-missing columns, and preserving Sprint 1 behavior.

I ran the Sprint 2 implementation with `uv run main.py data/datatest.csv`. The run still reported 262 rows and 19 columns, and it added a `Missing values:` section showing `closed_at: 72 missing (27.5%)` as the largest missing-value issue. I independently checked the CSV with a short Python `csv` module command and confirmed the same row count, column count, and nonzero missing-value counts.

I also reran Sprint 1 behavior checks: `uv run main.py data/missing.csv` still returned `Error: file not found: data\missing.csv`, and `uv run main.py` still showed that `csv_path` is required. These checks helped confirm that Sprint 2 added behavior without breaking the Sprint 1 command-line workflow.

The Sprint 2 definition of done was met. The tool still runs with the provided CSV path and preserves the Sprint 1 row count, column list, and preview. It now adds missing-value counts and percentages by column, sorted so the most-missing column appears first. The README also describes the new missing-value summary, and `SUBMISSION.md` records the implementation and verification.

Sprint 2 commit: `d630c53` (`Implement sprint 2 missing value summary`)
Sprint 2 push status: pushed manually to GitHub after commit `d630c53`.

## Workflow reflection

This practicum connected directly to Lecture 03A because Git helped me see and control my work as a sequence of intentional changes. Instead of editing everything at once, I used `git status`, `git diff`, and separate commits to check what changed before saving each sprint. That made the project feel safer because I could tell exactly what belonged to Sprint 1 and what belonged to Sprint 2.

Also, starting with a sprint spec changed how I used Codex. When I wrote the problem statement and user requirements first, Codex had a clearer target and stayed closer to the sprint goal. The specs helped me separate what the user needed from how the code would be implemented.

`uv` made running the project simple and repeatable. I used `uv run main.py data/datatest.csv` to test the tool without needing to manually manage a Python environment. That made it easier to focus on whether the tool worked instead of getting stuck on setup.

Watching Codex implement the sprints also helped me understand why inspection matters. I did not just accept the code; I checked the files, ran the commands, compared the output to the CSV, and reviewed the Git diff before committing.

## Practicum feedback

The most useful part of this practicum was practicing the full workflow from spec to implementation to inspection to commit. The most confusing part was GitHub authentication and pushing from the terminal, especially understanding tokens and why an interactive login prompt does not work the same way inside Codex.

## Unresolved question

None at this time.
