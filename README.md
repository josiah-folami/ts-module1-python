# ts-module1-python

## About Me

Hi, I'm **Folasayomi Udofia**, a learner in the **[TS Academy](https://app.tsacademyonline.com/enrollments)** Data Science Programme (Module 01: Python for Data Science).

## Project contents

### Gradebook

The `gradebook/` folder contains the Gradebook assignment:

- `gradebook/gradebook.py` reads student scores from a CSV file, assigns letter grades, prints the class count, mean, median, highest and lowest scores, and writes a report sorted by score.
- `gradebook/students.csv` is the sample input. Rows with non-numeric scores are skipped with a warning.
- `gradebook/report.txt` is the generated report.

### Exercises

Each short exercise is in its own folder under `exercises/`:

- `exercises/indoor/indoor.py` asks for text and prints it in lowercase.
- `exercises/tip/tip.py` calculates a tip from a meal cost and tip percentage.
- `exercises/bank/bank.py` prints `$0`, `$20`, or `$100` based on the greeting.
- `exercises/coke/coke.py` accepts 25-, 10-, and 5-cent coins for a 50-cent drink and reports the amount due or change owed.
- `exercises/fuel/fuel.py` converts a fraction to a percentage and prints `E` or `F` for very low or very high fuel levels.
- `exercises/lines/lines.py` counts nonblank, noncomment lines in a Python file.
- `exercises/scores/scores.py` reads `scores.csv` and prints the mean, median, highest-scoring student, and lowest-scoring student.
- `exercises/scores/scores.csv` contains the sample scores for `scores.py`.

## How to run

Run the exercise commands from the repository's top-level folder:

```bash
python exercises/indoor/indoor.py
python exercises/tip/tip.py
python exercises/bank/bank.py
python exercises/coke/coke.py
python exercises/fuel/fuel.py
python exercises/lines/lines.py gradebook/gradebook.py
python exercises/scores/scores.py
```

For `lines.py`, replace `gradebook/gradebook.py` with the `.py` file you want to count.

To run Gradebook, first change into its folder, then run it with the sample CSV:

```bash
cd gradebook
python gradebook.py students.csv
```

The Gradebook program writes `report.txt` in the current folder.
