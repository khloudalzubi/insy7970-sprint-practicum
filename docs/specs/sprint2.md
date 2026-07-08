# Sprint 1: Basic CSV Inspection

## Problem Statement

Build a Python command-line tool to inspect CSV files.

## User Requirements

Goals for this sprint as 3-5 concise, concrete user needs:

1. As a user, I can run the tool from the command line with a CSV file path.
2. As a user, I can see the CSV column names so I understand the file structure.
3. As a user, I can see the number of data rows in the CSV file.
4. As a user, I can see a small preview of the first few rows.
5. As a user, I receive a clear error message if the file path is missing or invalid.

## Plan

Implement a small command-line interface in Python using standard library modules. The tool will accept a CSV file path argument, read the file safely, count rows, display column headers, and print a short preview. Keep the implementation simple so the first sprint produces a working baseline that can be expanded in later sprints.

## Tasks

1. Update `main.py` to accept a CSV file path argument.
2. Validate that the provided path exists and points to a file.
3. Read the CSV with Python's `csv` module.
4. Print column names, total data row count, and a preview of the first few rows.
5. Verify the tool with the provided sample CSV.
6. Record the sprint outcome in `SUBMISSION.md`.

## Out of Scope

This sprint will not clean data, infer column types, detect duplicate identifiers, validate dates, or compute detailed statistics. It will also not add third-party dependencies or support non-CSV file formats.

## Definition of Done

The sprint is done when the command-line tool runs successfully against the provided CSV file, prints headers, row count, and a short preview, handles missing or invalid file paths with clear messages, and the completed work is summarized in `SUBMISSION.md`.
