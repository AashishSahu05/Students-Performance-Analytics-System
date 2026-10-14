# Project Documentation: Student Performance Analytics System

## 1. Project title and student details

**Project title:** Student Performance Analytics System  
**Student name:** [Enter your name]  
**Course:** Python with AI, EWB Courses  
**Student ID / batch:** [Enter if required]

## 2. Objective

The project reads student details, subject marks, and attendance from a CSV file and presents a simple analysis through a command-line menu. It is intended to make it easier to review individual totals and averages, grades, class pass/fail counts, toppers, and subject performance.

## 3. Technologies used

- Python
- Pandas, for reading and processing the CSV data
- NumPy, for subject-wise maximum, minimum, and mean calculations
- CSV, for storing the student dataset

## 4. Dataset description

The included `students.csv` contains 20 sample student records. Its fields are `Student_ID`, `Name`, `Department`, five subject mark columns (`Python`, `Mathematics`, `AI`, `Statistics`, `English`), and `Attendance`. Marks and attendance are represented as values from 0 to 100.

## 5. Implementation

1. Pandas loads `students.csv` into a DataFrame.
2. The program adds each student's total and average across the five subject columns.
3. The `Grades` function assigns a grade from the average. A+ begins at 90; A, B, C, D, and E cover descending ten-point bands; averages below 40 receive F.
4. The `Status` function returns Pass for an average of at least 40 and Fail otherwise.
5. A menu loop accepts a choice and displays a student total, average, grade and status, top five students, pass/fail counts, subject summaries, or the full report.
6. NumPy calculates subject highs, lows, and averages. Pandas filters records and sorts the topper list.

## 6. Key features

- Per-student total, average, grade, and pass/fail report
- Top five students sorted by total marks
- Class pass/fail count display
- Highest, lowest, and mean marks for each subject
- Full class report table
- 20-record sample dataset

## 7. Output / screenshots

The program displays text reports in PowerShell. Screenshots can be added here after running the program, for example under an `screenshots/` directory. No screenshots are included yet.

## 8. Final outcome

The project brings the sample student dataset and basic performance summaries into one interactive command-line program. It demonstrates CSV loading and data analysis using Pandas and NumPy, along with functions, conditions, and a menu loop.

## 9. Challenges and learning

This project practices reading tabular data, applying calculations to rows, assigning categories from numeric values, sorting records, filtering pass/fail results, and summarizing each subject. The supplied program has a few output limitations that should be reviewed: the fail count is displayed with a “Passed Students” label, the overall class-performance text is fixed, and individual records are selected by row index rather than student ID. The source was kept unchanged as requested.

## 10. GitHub repository

**Repository URL:** https://github.com/AashishSahu05/Students-Performance-Analytics-System  
**Google Form:** Submit the repository URL using the form provided by EWB Courses.

## Running the project

Install dependencies using `python -m pip install -r requirements.txt`, then run `python .\\main.py` from PowerShell in the project folder.

## Submission note

The project brief requests a GitHub repository, README, dataset, project documentation, and submission of the repository link through the EWB Courses Google Form. Replace the student and repository placeholders and complete the form submission before handing in the project.
