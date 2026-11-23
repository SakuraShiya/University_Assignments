# Write a Python Program To Create a Student Class, Make Objects By Taking Inputs From The User & Display Details Of All Students.

from math import isfinite

SUBJECTS: tuple[str, ...] = ("Physics", "Chemistry", "Mathematics")

class Student:
    """ Store The Name, SAP ID & Subject Marks Of One Student """

    def __init__(self, name: str, sap_id: str, marks: list[float]) -> None:
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    def display_details(self) -> None:
        """ Print The Student's Name, SAP ID & Marks In Each Subject """
        print(f"Name : {self.name}")
        print(f"SAP ID : {self.sap_id}")

        for subject, mark in zip(SUBJECTS, self.marks):
            print(f"{subject} : {mark:.2f}")

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Students : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    students: list[Student] = []

    for i in range(1, n + 1):
        print()
        name = input(f"Please Enter The Name Of Student {i} : ").strip()
        sap_id = input(f"Please Enter The SAP ID Of Student {i} : ").strip()

        if not name or not sap_id.isdecimal():
            print("Invalid Input, Name Cannot Be Empty & SAP ID Must Contain Only Digits.")
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

        students.append(Student(name, sap_id, marks))

    print()
    print("Details Of All Students Are As Follows :")

    for student in students:
        print()
        student.display_details()

if __name__ == "__main__":
    main()
