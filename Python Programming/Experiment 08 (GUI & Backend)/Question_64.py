# Write a Python Program To Design a GUI Based Basic Calculator For Performing Basic Arithmetic Operations.

from collections.abc import Callable
from math import isfinite
from tkinter import CENTER, END, Button, Entry, Frame, Label, Tk, messagebox

WINDOW_SIZE: str = "1280x720"

OPERATIONS: dict[str, Callable[[float, float], float]] = {
    "Add": lambda a, b: a + b,
    "Subtract": lambda a, b: a - b,
    "Multiply": lambda a, b: a * b,
    "Divide": lambda a, b: a / b,
}

def main() -> None:
    root = Tk()
    root.title("Basic Calculator")
    root.geometry(WINDOW_SIZE)

    frame = Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    for column in range(5):
        frame.columnconfigure(column, weight=1, uniform="equal")

    Label(frame, text="Enter First Number", bg="lightgray").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    entry_first = Entry(frame)
    entry_first.grid(row=0, column=2, columnspan=3, padx=10, pady=10)

    Label(frame, text="Enter Second Number", bg="lightgray").grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    entry_second = Entry(frame)
    entry_second.grid(row=1, column=2, columnspan=3, padx=10, pady=10)

    label_result = Label(frame, text="Result : ", bg="lightgray")
    label_result.grid(row=4, column=0, columnspan=5, padx=10, pady=10)

    def calculate(operation: str) -> None:
        """ Read Both Numbers, Apply The Chosen Operation & Show The Result """
        try:
            first = float(entry_first.get())
            second = float(entry_second.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please Enter Valid Numbers In Both Fields.")
            return

        if not (isfinite(first) and isfinite(second)):
            messagebox.showerror("Invalid Input", "Please Enter Finite Numbers In Both Fields.")
            return

        try:
            result = OPERATIONS[operation](first, second)
        except ZeroDivisionError:
            messagebox.showerror("Invalid Input", "Division By Zero Is Not Allowed.")
            return

        if not isfinite(result):
            messagebox.showerror("Invalid Input", "The Result Is Too Large To Represent.")
            return

        label_result.config(text=f"Result : {result:.2f}")

    def clear() -> None:
        """ Clear Both Input Fields & The Result """
        entry_first.delete(0, END)
        entry_second.delete(0, END)
        label_result.config(text="Result : ")

    Button(frame, text="Add", fg="green", command=lambda: calculate("Add")).grid(row=3, column=0, padx=10, pady=10, sticky="ew")
    Button(frame, text="Subtract", fg="green", command=lambda: calculate("Subtract")).grid(row=3, column=1, padx=10, pady=10, sticky="ew")
    Button(frame, text="Multiply", fg="green", command=lambda: calculate("Multiply")).grid(row=3, column=2, padx=10, pady=10, sticky="ew")
    Button(frame, text="Divide", fg="green", command=lambda: calculate("Divide")).grid(row=3, column=3, padx=10, pady=10, sticky="ew")
    Button(frame, text="Clear", fg="red", command=clear).grid(row=3, column=4, padx=10, pady=10, sticky="ew")

    root.mainloop()

if __name__ == "__main__":
    main()
