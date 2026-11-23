# Write a Python Program To Create a Tkinter GUI Task Manager Where Users Can Add, Edit & Remove Tasks Stored In SQLite.

from contextlib import closing
from pathlib import Path
from sqlite3 import DatabaseError, connect
from tkinter import END, Button, Entry, Event, Label, Tk, messagebox
from tkinter.ttk import Treeview

DATABASE_FILE: Path = Path(__file__).with_name("Task_Manager.db")
WINDOW_SIZE: str = "1280x720"

def create_table() -> None:
    """ Create The Tasks Table If It Does Not Already Exist """
    with closing(connect(DATABASE_FILE)) as connection:
        connection.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT NOT NULL)")
        connection.commit()

def fetch_tasks() -> list[tuple[int, str]]:
    """ Return Every Task As an (Id, Description) Tuple In The Order They Were Added """
    with closing(connect(DATABASE_FILE)) as connection:
        return connection.execute("SELECT id, description FROM tasks ORDER BY id").fetchall()

def insert_task(description: str) -> None:
    """ Add a New Task To The Database """
    with closing(connect(DATABASE_FILE)) as connection:
        connection.execute("INSERT INTO tasks (description) VALUES (?)", (description,))
        connection.commit()

def update_task(task_id: int, description: str) -> None:
    """ Change The Description Of The Task With The Given Id """
    with closing(connect(DATABASE_FILE)) as connection:
        connection.execute("UPDATE tasks SET description = ? WHERE id = ?", (description, task_id))
        connection.commit()

def delete_task(task_id: int) -> None:
    """ Remove The Task With The Given Id """
    with closing(connect(DATABASE_FILE)) as connection:
        connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        connection.commit()

def main() -> None:
    create_table()

    root = Tk()
    root.title("Task Manager")
    root.geometry(WINDOW_SIZE)

    tasks: dict[int, str] = {}

    Label(root, text="Task Description", bg="lightgray").pack(pady=10)
    entry_task = Entry(root, width=40)
    entry_task.pack(pady=5)

    tree_tasks = Treeview(root, columns=("number", "task"), show="headings", height=12, selectmode="browse")
    tree_tasks.heading("number", text="No.")
    tree_tasks.heading("task", text="Task Description")
    tree_tasks.column("number", width=60, anchor="center")
    tree_tasks.column("task", width=500)

    def refresh_tasks() -> None:
        """ Reload The Tasks From The Database & Show Them Numbered, Using Each Task's Id As Its Row Id """
        tasks.clear()
        tasks.update(fetch_tasks())
        tree_tasks.delete(*tree_tasks.get_children())

        for number, (task_id, description) in enumerate(tasks.items(), start=1):
            tree_tasks.insert("", END, iid=str(task_id), values=(number, description))

        entry_task.delete(0, END)

    def read_description() -> str | None:
        """ Return The Typed Description, Or Show An Error & Return None If It Is Empty """
        description = entry_task.get().strip()

        if not description:
            messagebox.showerror("Invalid Input", "Task Description Cannot Be Empty.")
            return None

        return description

    def selected_task_id() -> int | None:
        """ Return The Id Of The Selected Task, Or Show An Error & Return None If Nothing Is Selected """
        selection = tree_tasks.selection()

        if not selection:
            messagebox.showerror("Invalid Input", "Please Select a Task From The List First.")
            return None

        return int(selection[0])

    def is_duplicate(description: str, skip_id: int | None = None) -> bool:
        """ Check Whether Another Task Already Has This Description (Case Insensitive) """
        return any(
            task_id != skip_id and existing.lower() == description.lower()
            for task_id, existing in tasks.items()
        )

    def fill_entry(_event: Event[Treeview]) -> None:
        """ Copy The Selected Task Into The Entry So It Can Be Edited """
        selection = tree_tasks.selection()

        if selection:
            entry_task.delete(0, END)
            entry_task.insert(0, tasks[int(selection[0])])

    def add_task() -> None:
        """ Add The Typed Task If It Is Not Empty Or a Duplicate """
        description = read_description()

        if description is None:
            return

        if is_duplicate(description):
            messagebox.showerror("Invalid Input", f"The Task '{description}' Already Exists.")
            return

        try:
            insert_task(description)
        except DatabaseError as error:
            messagebox.showerror("Error Occurred", f"Could Not Add The Task ({error}).")
            return

        refresh_tasks()
        messagebox.showinfo("Success", "Task Added Successfully.")

    def edit_task() -> None:
        """ Replace The Selected Task With The Typed Description """
        task_id = selected_task_id()

        if task_id is None:
            return

        description = read_description()

        if description is None:
            return

        if is_duplicate(description, skip_id=task_id):
            messagebox.showerror("Invalid Input", f"The Task '{description}' Already Exists.")
            return

        try:
            update_task(task_id, description)
        except DatabaseError as error:
            messagebox.showerror("Error Occurred", f"Could Not Update The Task ({error}).")
            return

        refresh_tasks()
        messagebox.showinfo("Success", "Task Updated Successfully.")

    def remove_task() -> None:
        """ Remove The Selected Task After Asking For Confirmation """
        task_id = selected_task_id()

        if task_id is None:
            return

        if not messagebox.askyesno("Confirm Removal", f"Remove The Task '{tasks[task_id]}'?"):
            return

        try:
            delete_task(task_id)
        except DatabaseError as error:
            messagebox.showerror("Error Occurred", f"Could Not Remove The Task ({error}).")
            return

        refresh_tasks()
        messagebox.showinfo("Success", "Task Removed Successfully.")

    Button(root, text="Add Task", fg="green", command=add_task).pack(pady=5)
    Button(root, text="Edit Task", fg="blue", command=edit_task).pack(pady=5)
    Button(root, text="Remove Task", fg="red", command=remove_task).pack(pady=5)

    tree_tasks.pack(pady=10)
    tree_tasks.bind("<<TreeviewSelect>>", fill_entry)

    refresh_tasks()
    root.mainloop()

if __name__ == "__main__":
    main()
