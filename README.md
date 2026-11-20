# ts-module1-python

## About Me
Hi, I'm **Folasayomi Udofia**, a learner in the **[TS Academy](https://app.tsacademyonline.com/enrollments)** Data Science Programme (Module 01: Python for Data Science).

## What Each Program Does

### Gradebook (`gradebook/`)
- **`gradebook/gradebook.py`**: Takes a CSV file path on the command line (such as `students.csv`), validates arguments and file existence, reads rows using `csv.DictReader` into a list of dictionaries, skips non-numeric scores safely with a warning message, assigns letter grades (`A`: 90+, `B`: 80+, `C`: 70+, `D`: 60+, `F`: below 60) via `letter(score)`, prints summary statistics (student count, mean, median, highest, and lowest score using `statistics`), and writes a sorted `report.txt` from highest to lowest score.

### Exercises (`exercises/`)
- **`exercises/indoor/indoor.py`**: Prompts the user for input text and prints it back in lowercase.
- **`exercises/tip/tip.py`**: Prompts for a meal cost and a tip percentage, converts them using `dollars_to_float` and `percent_to_float`, and prints the calculated tip amount.
- **`exercises/bank/bank.py`**: Evaluates a greeting while ignoring case and leading spaces, printing `$0` if it starts with `hello`, `$20` if it starts with `h` (without being `hello`), and `$100` for anything else.
- **`exercises/coke/coke.py`**: Starts with a `50`-cent drink cost, accepts `25`, `10`, and `5` coins until paid in full, displays the remaining amount due after each coin, and prints any change owed at the end.
- **`exercises/fuel/fuel.py`**: Prompts for a fraction (such as `3/4`) and prints the fuel level as a percentage—displaying `E` for `1%` or less and `F` for `99%` or more—while handling `ValueError` and `ZeroDivisionError`.
- **`exercises/lines/lines.py`**: Accepts a `.py` filename on the command line and counts its lines of code while skipping blank lines and comment lines, exiting with a message if given invalid arguments or a missing file.
- **`exercises/scores/scores.py`**: Reads `scores.csv` (`name,score`) using `csv.DictReader` and `statistics`, then prints the mean, median, highest student/score, and lowest student/score.

## How to Run
Run the scripts from your terminal with Python 3:

```bash
python exercises/indoor/indoor.py
python exercises/tip/tip.py
python exercises/bank/bank.py
python exercises/coke/coke.py
python exercises/fuel/fuel.py
python exercises/lines/lines.py path/to/script.py
python exercises/scores/scores.py
python gradebook/gradebook.py gradebook/students.csv
