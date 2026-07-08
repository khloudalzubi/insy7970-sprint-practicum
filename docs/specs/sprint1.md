# Sprint 1: Basic CSV Inspection

## Problem Statement

Build a Python command-line tool to inspect CSV files.

## User Requirements

1. The user can provide a CSV file path.
2. The tool reports the row count.
3. The project includes basic run instructions.
4. The tool shows the column names.
5. The tool shows a small preview of the first few rows.

## Plan

Create a small command-line CSV inspection tool using Python's standard library. The tool will accept a CSV path from the command line, validate that the path exists, read the file with the `csv` module, and print a short summary that includes column names, row count, and a preview of the first few rows. Keep Sprint 1 focused on a reliable first increment: basic input, basic output, and basic instructions.

## Tasks

1. Update `main.py` so the user can pass a CSV file path from the command line.
2. Add friendly handling for a missing file path or a path that does not exist.
3. Read the provided CSV file with Python's `csv` module.
4. Print the CSV column names.
5. Count and print the number of data rows, excluding the header row.
6. Print a small preview of the first few data rows.
7. Add basic run instructions to `README.md`.
8. Verify the tool with `uv run main.py data/datatest.csv`.
9. Record the sprint outcome and checks in `SUBMISSION.md`.

## Out of Scope

This sprint will not clean data, infer column types, detect duplicate identifiers, validate dates, or compute detailed statistics. It will not add third-party dependencies, modify the source CSV, or support non-CSV file formats. More detailed data-quality checks belong in a later sprint.

## Definition of Done

Sprint 1 is done when the tool can be run from the command line with the provided CSV path, reports the row count, shows column names, and prints a short row preview. The README includes basic run instructions, invalid or missing paths produce clear messages, and `SUBMISSION.md` summarizes the sprint decisions and verification.