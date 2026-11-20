# Write a Python Program To Generate a Student Grade Sheet Based On Marks Obtained.

from math import isfinite

SUBJECTS: tuple[str, ...] = ("English", "Physics", "Chemistry", "Mathematics", "Computer Science")

def get_grade(cgpa: float) -> str:
    """ Return The Grade Based On CGPA """
    if cgpa >= 9.0:
        return "O"
    elif cgpa >= 8.0:
        return "A+"
    elif cgpa >= 7.0:
        return "A"
    elif cgpa >= 6.0:
        return "B"
    elif cgpa >= 5.0:
        return "C"
    else:
        return "F"

def display_grade_sheet(name: str, total_marks: float, percentage: float, cgpa: float, grade: str) -> None:
    """ Display The Student Grade Sheet """
    print(f"Student Name : {name}")
    print(f"Total Marks : {total_marks:.2f} / {len(SUBJECTS) * 100}")
    print(f"Percentage : {percentage:.2f} %")
    print(f"CGPA : {cgpa:.2f}")
    print(f"Grade Obtained : {grade}")

def main() -> None:
    name = input("Please Enter The Student Name : ").strip()

    if not name:
        print("Invalid Input, Student Name Cannot Be Empty.")
        return

    marks: list[float] = []

    for subject in SUBJECTS:
        try:
            mark = float(input(f"Please Enter The Marks Obtained In {subject} : "))
        except ValueError:
            print(f"Invalid Input, Please Enter a Valid Number For Marks Obtained In {subject}.")
            return

        if not isfinite(mark) or not (0 <= mark <= 100):
            print(f"Invalid Input, Please Enter Finite Marks Between 0 & 100 For {subject}.")
            return

        marks.append(mark)

    total_marks = sum(marks)
    percentage = total_marks / len(marks)
    cgpa = percentage / 10

    grade = get_grade(cgpa)
    display_grade_sheet(name, total_marks, percentage, cgpa, grade)

if __name__ == "__main__":
    main()
