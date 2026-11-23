# Write a Python Program To Design a Tkinter GUI For Student Course Registration & Store The Details In a SQLite Database.

from contextlib import closing
from pathlib import Path
from sqlite3 import DatabaseError, connect
from tkinter import CENTER, END, Button, Entry, Frame, Label, Tk, messagebox

DATABASE_FILE: Path = Path(__file__).with_name("Student_Registration.db")
WINDOW_SIZE: str = "1280x720"
MIN_AGE: int = 18
MAX_AGE: int = 25

def create_table() -> None:
    """ Create The Students Table If It Does Not Already Exist """
    with closing(connect(DATABASE_FILE)) as connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS students ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER NOT NULL, course TEXT NOT NULL)"
        )
        connection.commit()

def save_student(name: str, age: int, course: str) -> None:
    """ Insert One Student Record Into The Students Table """
    with closing(connect(DATABASE_FILE)) as connection:
        connection.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
        connection.commit()

def main() -> None:
    create_table()

    root = Tk()
    root.title("Student Registration")
    root.geometry(WINDOW_SIZE)

    frame = Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Name Of Student", bg="lightgray").grid(row=0, column=0, padx=10, pady=10)
    entry_name = Entry(frame)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    Label(frame, text="Age Of Student", bg="lightgray").grid(row=1, column=0, padx=10, pady=10)
    entry_age = Entry(frame)
    entry_age.grid(row=1, column=1, padx=10, pady=10)

    Label(frame, text="Course Of Student", bg="lightgray").grid(row=2, column=0, padx=10, pady=10)
    entry_course = Entry(frame)
    entry_course.grid(row=2, column=1, padx=10, pady=10)

    def clear_fields() -> None:
        """ Clear All Input Fields & Move The Cursor Back To The Name Field """
        entry_name.delete(0, END)
        entry_age.delete(0, END)
        entry_course.delete(0, END)
        entry_name.focus_set()

    def register_student() -> None:
        """ Validate The Form & Save The Student To The Database """
        name = entry_name.get().strip()
        age_text = entry_age.get().strip()
        course = entry_course.get().strip()

        if not name or not age_text or not course:
            messagebox.showerror("Invalid Input", "All Fields Are Required.")
            return

        try:
            age = int(age_text)
        except ValueError:
            messagebox.showerror("Invalid Input", "Age Must Be a Whole Number.")
            return

        if not (MIN_AGE <= age <= MAX_AGE):
            messagebox.showerror("Invalid Input", f"Age Must Be Between {MIN_AGE} & {MAX_AGE}.")
            return

        try:
            save_student(name, age, course)
        except DatabaseError as error:
            messagebox.showerror("Error Occurred", f"Could Not Save The Student ({error}).")
            return

        messagebox.showinfo("Success", f"{name} Has Been Registered For {course} Successfully.")
        clear_fields()

    Button(frame, text="Register", fg="green", command=register_student).grid(row=3, column=0, padx=10, pady=10)
    Button(frame, text="Clear", fg="red", command=clear_fields).grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
