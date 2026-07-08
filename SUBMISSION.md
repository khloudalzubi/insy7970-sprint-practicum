# Practicum 3 Submission

Operating system: Windows
Terminal used: PowerShell and Git Bash
Codex tool used: Codex desktop app
GitHub repository URL:

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

## Workflow reflection

## Practicum feedback

## Unresolved question
