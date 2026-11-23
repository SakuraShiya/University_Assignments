# Write a Python Program To Design a Login & Signup Authentication System Using Tkinter & SQLite.

from contextlib import closing
from hashlib import pbkdf2_hmac
from pathlib import Path
from secrets import token_hex
from sqlite3 import DatabaseError, IntegrityError, connect
from tkinter import CENTER, END, Button, Entry, Frame, Label, Tk, messagebox

DATABASE_FILE: Path = Path(__file__).with_name("Users.db")
WINDOW_SIZE: str = "1280x720"
MIN_PASSWORD_LENGTH: int = 6
HASH_ITERATIONS: int = 100_000

def hash_password(password: str, salt: str) -> str:
    """ Return The Salted PBKDF2 Hash Of The Password, So The Plain Password Is Never Stored """
    return pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(salt), HASH_ITERATIONS).hex()

def create_table() -> None:
    """ Create The Users Table If It Does Not Already Exist (Usernames Are Case Insensitive) """
    with closing(connect(DATABASE_FILE)) as connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS users ("
            "username TEXT PRIMARY KEY COLLATE NOCASE, salt TEXT NOT NULL, password_hash TEXT NOT NULL)"
        )
        connection.commit()

def create_user(username: str, password: str) -> bool:
    """ Store a New User With a Random Salt, Returning False If The Username Is Already Taken """
    salt = token_hex(16)

    try:
        with closing(connect(DATABASE_FILE)) as connection:
            connection.execute("INSERT INTO users VALUES (?, ?, ?)", (username, salt, hash_password(password, salt)))
            connection.commit()
    except IntegrityError:
        return False

    return True

def check_login(username: str, password: str) -> bool:
    """ Return True Only If The Username Exists & The Password Hashes To The Stored Value """
    with closing(connect(DATABASE_FILE)) as connection:
        row = connection.execute("SELECT salt, password_hash FROM users WHERE username = ?", (username,)).fetchone()

    return row is not None and hash_password(password, row[0]) == row[1]

def main() -> None:
    create_table()

    root = Tk()
    root.title("Login & Signup Authentication System")
    root.geometry(WINDOW_SIZE)

    frame = Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Username", bg="lightgray").grid(row=0, column=0, padx=10, pady=10)
    entry_username = Entry(frame, width=30)
    entry_username.grid(row=0, column=1, padx=10, pady=10)

    Label(frame, text="Password", bg="lightgray").grid(row=1, column=0, padx=10, pady=10)
    entry_password = Entry(frame, show="*", width=30)
    entry_password.grid(row=1, column=1, padx=10, pady=10)

    def read_fields() -> tuple[str, str] | None:
        """ Return The Username & Password, Or Show An Error & Return None If Either Is Empty """
        username = entry_username.get().strip()
        password = entry_password.get()

        if not username or not password:
            messagebox.showerror("Invalid Input", "Username & Password Cannot Be Empty.")
            return None

        return username, password

    def signup() -> None:
        """ Create a New Account If The Password Is Long Enough & The Username Is Free """
        fields = read_fields()

        if fields is None:
            return

        username, password = fields

        if len(password) < MIN_PASSWORD_LENGTH:
            messagebox.showerror("Invalid Input", f"Password Must Be At Least {MIN_PASSWORD_LENGTH} Characters Long.")
            return

        try:
            created = create_user(username, password)
        except DatabaseError as error:
            messagebox.showerror("Error Occurred", f"Could Not Create The Account ({error}).")
            return

        if not created:
            messagebox.showerror("Invalid Input", f"The Username '{username}' Already Exists.")
            return

        entry_password.delete(0, END)
        messagebox.showinfo("Success", "Signup Successful, You Can Now Log In.")

    def login() -> None:
        """ Check The Username & Password Against The Stored Hash """
        fields = read_fields()

        if fields is None:
            return

        username, password = fields

        try:
            valid = check_login(username, password)
        except DatabaseError as error:
            messagebox.showerror("Error Occurred", f"Could Not Check The Login ({error}).")
            return

        entry_password.delete(0, END)

        if valid:
            messagebox.showinfo("Success", f"Login Successful, Welcome {username}.")
        else:
            messagebox.showerror("Invalid Input", "Incorrect Username Or Password.")

    Button(frame, text="Signup", fg="blue", command=signup).grid(row=2, column=0, padx=10, pady=10)
    Button(frame, text="Login", fg="green", command=login).grid(row=2, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
