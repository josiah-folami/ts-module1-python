import csv
import statistics
import sys


def letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def read_students(filename):
    students = []

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                score = float(row["score"])
            except (ValueError, TypeError, KeyError):
                print(f"Skipping {row.get('name', 'unknown')}: score is not a number")
                continue

            student = {
                "name": row.get("name", "Unknown"),
                "course": row.get("course", ""),
                "score": score,
                "grade": letter(score),
            }
            students.append(student)

    return students


def print_summary(students):
    scores = [student["score"] for student in students]
    highest = max(students, key=lambda student: student["score"])
    lowest = min(students, key=lambda student: student["score"])

    print(f"Students: {len(students)}")
    print(f"Mean: {statistics.mean(scores)}")
    print(f"Median: {statistics.median(scores)}")
    print(f"Highest: {highest['name']} ({highest['score']:g})")
    print(f"Lowest: {lowest['name']} ({lowest['score']:g})")


def write_report(students, filename="report.txt"):
    sorted_students = sorted(
        students,
        key=lambda student: student["score"],
        reverse=True,
    )

    with open(filename, "w", encoding="utf-8") as file:
        for student in sorted_students:
            file.write(
                f"{student['name']},{student['score']:g},{student['grade']}" + chr(10)
            )

    print(f"Report saved to {filename}")


def main():
    if len(sys.argv) == 1:
        print("Please provide a CSV filename.")
        return

    if len(sys.argv) > 2:
        print("Please provide only one filename.")
        return

    filename = sys.argv[1]

    if not filename.lower().endswith(".csv"):
        print("The file must be a .csv file.")
        return

    try:
        students = read_students(filename)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return
    except OSError as error:
        print(f"Could not read the file: {error}")
        return

    if not students:
        print("No valid student scores were found.")
        return

    print_summary(students)

    try:
        write_report(students)
    except OSError as error:
        print(f"Could not write the report: {error}")


if __name__ == "__main__":
    main()
