import csv
import statistics
from pathlib import Path


def main():
    csv_file = Path(__file__).parent / "scores.csv"
    students = []

    try:
        with open(csv_file, newline="", encoding="utf-8") as file:
            for row in csv.DictReader(file):
                try:
                    students.append({
                        "name": row["name"],
                        "score": int(row["score"]),
                    })
                except (ValueError, KeyError):
                    print(f"Skipping invalid row: {row}")
    except OSError as error:
        print(f"Could not read scores.csv: {error}")
        return

    if not students:
        print("No valid scores found.")
        return

    scores = [student["score"] for student in students]
    highest = max(students, key=lambda student: student["score"])
    lowest = min(students, key=lambda student: student["score"])

    print(f"Mean: {statistics.mean(scores)}")
    print(f"Median: {statistics.median(scores)}")
    print(f"Highest: {highest['name']} ({highest['score']})")
    print(f"Lowest: {lowest['name']} ({lowest['score']})")


if __name__ == "__main__":
    main()