# insy7970-sprint-practicum

Command-line CSV inspection tool built through supervised practicum sprints.

## Run

Inspect the provided sample CSV:

```powershell
uv run main.py data/datatest.csv
```

Inspect another CSV file by passing its path:

```powershell
uv run main.py path\to\file.csv
```

The tool prints the CSV row count, column names, a preview of the first few data rows, and a missing-value summary for each column. Missing-value counts treat blank cells and whitespace-only cells as missing.