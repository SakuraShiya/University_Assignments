# Write a Python Program To Create Multiple Suitable Exceptions For a File Handling Program.

def create_file() -> None:
    """ Create a New File In 'x' Mode, Which Raises FileExistsError Instead Of Overwriting An Existing File """
    file_name = input("Please Enter The File Name To Create : ").strip()

    if not file_name:
        print("Invalid Input, File Name Cannot Be Empty.")
        return

    data = input("Please Enter The Data To Write : ")

    try:
        with open(file_name, "x", encoding="utf-8") as file:
            file.write(data + "\n")
    except FileExistsError:
        print(f"Invalid Input, '{file_name}' Already Exists & Will Not Be Overwritten.")
    except PermissionError:
        print(f"Error Occurred, You Do Not Have Permission To Create '{file_name}'.")
    except OSError as error:
        print(f"Error Occurred, Could Not Create '{file_name}' ({error.strerror or error}).")
    else:
        print(f"File '{file_name}' Created Successfully.")

def append_file() -> None:
    """ Append Data To The End Of a File, Creating The File If It Does Not Exist """
    file_name = input("Please Enter The File Name To Append To : ").strip()

    if not file_name:
        print("Invalid Input, File Name Cannot Be Empty.")
        return

    data = input("Please Enter The Data To Append : ")

    try:
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(data + "\n")
    except FileNotFoundError:
        print(f"Invalid Input, The Folder For '{file_name}' Does Not Exist.")
    except PermissionError:
        print(f"Error Occurred, You Do Not Have Permission To Append To '{file_name}' (Or It Is a Folder).")
    except OSError as error:
        print(f"Error Occurred, Could Not Append To '{file_name}' ({error.strerror or error}).")
    else:
        print(f"Data Appended To '{file_name}' Successfully.")

def read_file() -> None:
    """ Read & Display a Text File, Handling Missing, Protected, Folder & Non Text Files """
    file_name = input("Please Enter The File Name To Read : ").strip()

    if not file_name:
        print("Invalid Input, File Name Cannot Be Empty.")
        return

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Invalid Input, '{file_name}' Does Not Exist.")
    except IsADirectoryError:
        print(f"Invalid Input, '{file_name}' Is a Folder, Not a File.")
    except PermissionError:
        print(f"Error Occurred, You Do Not Have Permission To Read '{file_name}' (Or It Is a Folder).")
    except UnicodeDecodeError:
        print(f"Invalid Input, '{file_name}' Is Not a Text File.")
    except OSError as error:
        print(f"Error Occurred, Could Not Read '{file_name}' ({error.strerror or error}).")
    else:
        print(f"Contents Of '{file_name}' :")
        print(content.rstrip() if content.strip() else "(The File Is Empty)")

def main() -> None:
    print("Create a New File :")
    create_file()

    print()
    print("Append To a File :")
    append_file()

    print()
    print("Read a File :")
    read_file()

if __name__ == "__main__":
    main()
