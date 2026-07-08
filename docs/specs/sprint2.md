# Sprint 2: Missing Value Summary

## Problem Statement

Build on the basic CSV inspection tool by adding a data-quality summary that helps users quickly identify missing values in a CSV file.

## User Requirements

1. The tool reports the number of missing values for each column.
2. The tool reports the missing-value percentage for each column.
3. The tool treats blank cells and whitespace-only cells as missing.
4. The tool identifies the columns with the highest missing-value rates.
5. The Sprint 1 summary output still shows row count, column names, and a preview.

## Plan

Extend the existing CSV reading loop so it tracks missing values while preserving the Sprint 1 summary behavior. Missing values will be counted per column when a cell is empty or contains only whitespace. After the row count, column names, and preview, the tool will print a missing-value summary sorted by the highest missing percentage so the most important data-quality issues are easiest to see.

## Tasks

1. Update `main.py` to count blank and whitespace-only values per column.
2. Handle rows that are shorter than the header by counting omitted trailing cells as missing.
3. Print missing counts and percentages for each column.
4. Sort the missing-value summary so columns with the highest missing-value percentage appear first.
5. Keep the Sprint 1 output for file path input, row count, column names, and preview.
6. Update `README.md` to mention the missing-value summary.
7. Verify the provided CSV still reports 262 rows and 19 columns.
8. Verify at least one known missing value appears in the missing-value summary.
9. Record the Sprint 2 outcome and checks in `SUBMISSION.md`.

## Out of Scope

This sprint will not fill missing values, modify the CSV file, normalize inconsistent capitalization, validate dates, detect duplicates, or compute numeric statistics. It will not add third-party dependencies or change the command-line interface beyond the existing file path input.

## Definition of Done

Sprint 2 is done when the tool still runs with the provided CSV path, preserves the Sprint 1 row count, column list, and preview, and adds a missing-value summary with counts and percentages by column. The output should make columns with the most missing values easy to spot, the README should mention the new behavior, and `SUBMISSION.md` should summarize the implementation and verification.