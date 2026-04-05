# part1_grade_tracker.py
# Assignment Part 1 - Python Basics & Control Flow
# Theme : Student Grade Tracker
# just building a simple command line tracker that handles student data,
# computes results and prints a summary - all using core python concepts


# ─────────────────────────────────────────────────────────────────────
# TASK 1  -  Data Parsing & Profile Cleaning
# ─────────────────────────────────────────────────────────────────────

print("=" * 58)
print("TASK 1 - Data Parsing & Profile Cleaning")
print("=" * 58)

# raw data given to us - names have weird spacing and casing,
# roll numbers are strings, and marks are all in one comma separated string
# basically messy data like you'd get from a google form or something
raw_students = [
    {"name": "  ayesha sharma ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": " ronit verma",     "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "PRIYA NAIR  ",     "roll": "103", "marks_str": "81, 85, 88, 94, 79"},
    {"name": "karan mehta",      "roll": "104", "marks_str": "48, 55, 38, 62, 50"},
    {"name": "  sneha pillai ",  "roll": "105", "marks_str": "75, 80, 78, 68, 85"},
]

cleaned_students = []  # will store cleaned versions here

for student in raw_students:

    # strip whitespace from both ends then title case it
    clean_name = student["name"].strip().title()

    # roll was stored as string, converting to int
    clean_roll = int(student["roll"])

    # split the marks string on comma and convert each piece to int
    clean_marks = [int(m.strip()) for m in student["marks_str"].split(",")]

    cleaned = {
        "name": clean_name,
        "roll": clean_roll,
        "marks": clean_marks
    }
    cleaned_students.append(cleaned)

    # check if every word in the name is purely alphabetic
    # something like "O'Brien" would fail this check, which is fine for now
    words = clean_name.split()
    is_valid = all(word.isalpha() for word in words)
    validity_tag = "V Valid name" if is_valid else "X Invalid name"

    # print the profile card for each student
    print(f"\n{validity_tag}")
    print(f"  Student  : {clean_name}")
    print(f"  Roll No  : {clean_roll}")
    print(f"  Marks    : {clean_marks}")

# specifically printing roll 103's name in upper and lower case
print("\n-- Roll No 103 Name Cases --")
for s in cleaned_students:
    if s["roll"] == 103:
        print(f"  UPPER  : {s['name'].upper()}")
        print(f"  lower  : {s['name'].lower()}")


# ─────────────────────────────────────────────────────────────────────
# TASK 2  -  Marks Analysis Using Loops & Conditionals
# ─────────────────────────────────────────────────────────────────────

print("\n" + "=" * 58)
print("TASK 2 - Marks Analysis Using Loops & Conditionals")
print("=" * 58)

# using ayesha sharma's data for this task
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]


def get_grade(score):
    # grade scheme as given in the assignment
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "F"   # below 60 is a fail


# 1. printing each subject with its marks and grade
print(f"\nSubject wise report for {student_name}:")
print(f"  {'Subject':<12}  {'Marks':>5}   Grade")
print("  " + "-" * 28)
for subj, mark in zip(subjects, marks):
    print(f"  {subj:<12}  {mark:>5}   {get_grade(mark)}")

# 2. overall stats - total, average, best and worst subject
total   = sum(marks)
average = round(total / len(marks), 2)
best_i  = marks.index(max(marks))
worst_i = marks.index(min(marks))

print(f"\n  Total marks     : {total}")
print(f"  Average marks   : {average}")
print(f"  Best subject    : {subjects[best_i]} ({marks[best_i]})")
print(f"  Worst subject   : {subjects[worst_i]} ({marks[worst_i]})")

# 3. while loop - simulating a marks entry system
# in actual use you'd take input() here but for demo purposes i'm
# using a list of preset inputs so the script can run without stopping
print("\n-- Marks Entry System (type 'done' to stop) --")
print("  (running with simulated inputs for demo)\n")

new_subjects = list(subjects)
new_marks    = list(marks)
added        = 0

simulated = [
    ("Biology", "82"),
    ("Hindi",   "abc"),   # this one is invalid - non numeric
    ("History", "150"),   # out of range, should be rejected
    ("done",    ""),
]

idx = 0
while True:
    sub_in, mrk_in = simulated[idx]
    idx += 1

    print(f"  Subject name : {sub_in}")
    if sub_in.lower() == "done":
        break

    print(f"  Marks (0-100): {mrk_in}")

    try:
        m = int(mrk_in)
        if not (0 <= m <= 100):
            raise ValueError("out of range")
        new_subjects.append(sub_in)
        new_marks.append(m)
        added += 1
        print(f"  Added {sub_in} successfully with {m} marks\n")
    except ValueError:
        # just warn the user, dont crash and dont add it
        print(f"  Warning - '{mrk_in}' is not valid. Needs to be a number between 0 and 100. Skipping.\n")

updated_avg = round(sum(new_marks) / len(new_marks), 2)
print(f"  Subjects added   : {added}")
print(f"  Updated average  : {updated_avg}")


# ─────────────────────────────────────────────────────────────────────
# TASK 3  -  Class Performance Summary
# ─────────────────────────────────────────────────────────────────────

print("\n" + "=" * 58)
print("TASK 3 - Class Performance Summary")
print("=" * 58)

class_data = [
    ("Ayesha Sharma", [88, 72, 95, 68, 78]),
    ("Ronit Verma",   [55, 68, 43, 72, 61]),
    ("Priya Nair",    [81, 85, 88, 94, 79]),
    ("Karan Mehta",   [48, 55, 38, 62, 50]),
    ("Sneha Pillai",  [75, 80, 78, 68, 85]),
]

# compute average and pass/fail for each student
results = []
for name, m_list in class_data:
    avg    = round(sum(m_list) / len(m_list), 2)
    status = "Pass" if avg >= 60 else "Fail"
    results.append({"name": name, "average": avg, "status": status})

# print formatted class report table
print(f"\n  {'Name':<18}  {'Average':>8}   Status")
print("  " + "-" * 36)
for r in results:
    print(f"  {r['name']:<18}  {r['average']:>8}   {r['status']}")

# extra summary stats below the table
passed_list = [r for r in results if r["status"] == "Pass"]
failed_list = [r for r in results if r["status"] == "Fail"]
topper      = max(results, key=lambda x: x["average"])
cls_avg     = round(sum(r["average"] for r in results) / len(results), 2)

print(f"\n  Passed           : {len(passed_list)}")
print(f"  Failed           : {len(failed_list)}")
print(f"  Class topper     : {topper['name']} (avg {topper['average']})")
print(f"  Class average    : {cls_avg}")


# ─────────────────────────────────────────────────────────────────────
# TASK 4  -  String Manipulation
# ─────────────────────────────────────────────────────────────────────

print("\n" + "=" * 58)
print("TASK 4 - String Manipulation Utility")
print("=" * 58)

essay = ("  python is a versatile language. it supports object oriented, "
         "functional, and procedural programming. python is widely used in "
         "data science  ")

# step 1 - strip the leading and trailing whitespace first,
# then use clean_essay for everything below
clean_essay = essay.strip()
print(f"\nStep 1 - stripped:\n  '{clean_essay}'")

# step 2 - convert to title case
print(f"\nStep 2 - Title Case:\n  '{clean_essay.title()}'")

# step 3 - count how many times 'python' appears (case insensitive)
# since clean_essay is already lowercase, .count("python") works directly
count = clean_essay.count("python")
print(f"\nStep 3 - 'python' appears {count} time(s)")

# step 4 - replace every occurance of python with Python 🐍
# using clean_essay from step 1 since its already lowercase
replaced = clean_essay.replace("python", "Python 🐍")
print(f"\nStep 4 - after replace:\n  '{replaced}'")

# step 5 - split into sentences on '. ' (period + space)
sentences = clean_essay.split(". ")
print(f"\nStep 5 - sentences list:\n  {sentences}")

# step 6 - print numbered, making sure each ends with a full stop
print(f"\nStep 6 - numbered sentences:")
for i, s in enumerate(sentences, 1):
    s = s if s.endswith(".") else s + "."
    print(f"  {i}. {s}")

print("\n" + "=" * 58)
print("Part 1 done.")
print("=" * 58)
