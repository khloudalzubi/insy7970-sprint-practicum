import argparse
import csv
from pathlib import Path


PREVIEW_ROWS = 5


def inspect_csv(csv_path: Path) -> int:
    """Print a short summary of a CSV file."""
    with csv_path.open(newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        try:
            headers = next(reader)
        except StopIteration:
            print(f"CSV file: {csv_path}")
            print("Rows: 0")
            print("Columns: none")
            print("Preview: no data rows")
            return 0

        preview_rows = []
        row_count = 0
        for row in reader:
            row_count += 1
            if len(preview_rows) < PREVIEW_ROWS:
                preview_rows.append(row)

    print(f"CSV file: {csv_path}")
    print(f"Rows: {row_count}")
    print(f"Columns ({len(headers)}): {', '.join(headers)}")
    print("Preview:")

    if not preview_rows:
        print("  no data rows")
        return 0

    for index, row in enumerate(preview_rows, start=1):
        values = []
        for header, value in zip(headers, row):
            values.append(f"{header}={value}")
        if len(row) > len(headers):
            values.append(f"extra_values={row[len(headers):]}")
        print(f"  {index}. " + "; ".join(values))

    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect a CSV file and print a short summary."
    )
    parser.add_argument("csv_path", help="Path to the CSV file to inspect")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    csv_path = Path(args.csv_path)

    if not csv_path.exists():
        print(f"Error: file not found: {csv_path}")
        return 1

    if not csv_path.is_file():
        print(f"Error: path is not a file: {csv_path}")
        return 1

    try:
        return inspect_csv(csv_path)
    except csv.Error as error:
        print(f"Error: could not read CSV file: {error}")
        return 1
    except UnicodeDecodeError as error:
        print(f"Error: could not decode CSV file as UTF-8: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())