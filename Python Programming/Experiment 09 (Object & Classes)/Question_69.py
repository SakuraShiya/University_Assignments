# Write a Python Program To Add a Constructor To The Student Class & Show Details, Percentage, Pass/Fail Result & Class Average.

from math import isfinite

SUBJECTS: tuple[str, ...] = ("Physics", "Chemistry", "Mathematics")
PASS_MARK: float = 40

class Student:
    """ Store a Student's Details & Calculate Their Percentage & Result """

    def __init__(self, name: str, sap_id: str, marks: list[float]) -> None:
        self.name = name
        self.sap_id = sap_id
        self.marks = marks

    @property
    def percentage(self) -> float:
        """ The Average Of All Subject Marks, As Each Subject Is Out Of 100 """
        return sum(self.marks) / len(self.marks)

    @property
    def has_passed(self) -> bool:
        """ True Only If The Marks Are Greater Than The Pass Mark In Every Subject """
        return all(mark > PASS_MARK for mark in self.marks)

    def display(self) -> None:
        """ Print The Student's Details, Marks, Percentage & Result """
        print(f"Name : {self.name}")
        print(f"SAP ID : {self.sap_id}")

        for subject, mark in zip(SUBJECTS, self.marks):
            print(f"{subject} : {mark:.2f}")

        print(f"Percentage : {self.percentage:.2f} %")
        print(f"Result : {'Pass' if self.has_passed else 'Fail'}")

def class_average(students: list[Student]) -> float:
    """ Return The Average Percentage Of All Students In The Class """
    return sum(student.percentage for student in students) / len(students)

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

        if any(student.sap_id == sap_id for student in students):
            print(f"Invalid Input, SAP ID {sap_id} Has Already Been Entered.")
            return

        marks: list[float] = []

        for subject in SUBJECTS:
            try:
                mark = float(input(f"Please Enter The Marks Obtained In {subject} (Out Of 100) : "))
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
        student.display()

    passed = sum(1 for student in students if student.has_passed)

    print()
    print(f"Students Passed : {passed} Of {len(students)}")
    print(f"Overall Average Percentage Of The Class : {class_average(students):.2f} %")

if __name__ == "__main__":
    main()
