# Write a Python Program To Create a Simple Tkinter Window With a Title & Fixed Size.

from tkinter import Tk

WINDOW_TITLE: str = "Simple Tkinter Window"
WINDOW_SIZE: str = "1280x720"

def main() -> None:
    root = Tk()
    root.title(WINDOW_TITLE)
    root.geometry(WINDOW_SIZE)
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()
