# Student Performance Analytics System

A command-line Python project that loads a student marks dataset and offers student reports, a toppers list, class pass/fail counts, subject-wise summaries, and a complete class report.

## Requirements

- Python 3.10 or newer
- NumPy
- Pandas

Install the dependencies with:

```powershell
python -m pip install -r requirements.txt
```

## Run

Open PowerShell in the project folder and run:

```powershell
python .\main.py
```

Choose a menu option by entering its number. The current program uses each student's zero-based CSV row index for the individual report options. Choose `8` to exit.

## Dataset

`students.csv` contains 20 sample student records, including student ID, name, department, five subject marks, and attendance percentage. Marks are on a 0-100 scale.

## Grading and pass rule

The program calculates total and average marks across Python, Mathematics, AI, Statistics, and English. Grades are assigned from the average: A+ (90+), A (80-89.99), B (70-79.99), C (60-69.99), D (50-59.99), E (40-49.99), and F (below 40). An average of 40 or above is considered a pass.

## Project documentation

See [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md) for the objective, implementation, dataset, features, results, learning notes, and submission details.

## Known limitations

The source file is preserved as supplied. The pass/fail statistics menu currently labels both counts as “Passed Students”; the second count is the fail count. The class performance message is fixed text, and individual reports use row indexes rather than the `Student_ID` field. The code has not been edited to correct these behaviors.

## Repository and form submission

Repository: https://github.com/AashishSahu05/Students-Performance-Analytics-System. Submit this URL through the Google Form provided by EWB Courses.
