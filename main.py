
import csv
from pathlib import Path


def check_missing_values(file_path):
    with open(file_path, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        if not reader.fieldnames:
            raise ValueError("CSV file has no header.")

        missing_counts = {column: 0 for column in reader.fieldnames}
        total_rows = 0

        for row in reader:
            total_rows += 1
            for column in reader.fieldnames:
                value = row.get(column)
                if value is None or value.strip() == "":
                    missing_counts[column] += 1

    return total_rows, missing_counts


if __name__ == "__main__":
    file_path = Path("sample_data/sample.csv")

    if not file_path.exists():
        print(f"File not found: {file_path}")
    else:
        rows, missing = check_missing_values(file_path)
        print(f"Total rows: {rows}")
        print("Missing values by column:")
        for column, count in missing.items():
            print(f"  {column}: {count}")
