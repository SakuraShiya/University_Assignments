# Write a Python Program To Create a To-Do List Manager Where Users Can Add, View & Remove Tasks (Use List For Storing Tasks).

def is_duplicate_task(tasks: list[str], task: str) -> bool:
    """ Check Whether The Task Already Exists In The List (Case Insensitive) """
    return task.lower() in (existing.lower() for existing in tasks)

def display_tasks(tasks: list[str]) -> None:
    """ Display All Tasks With Their Task Numbers Or a Message If The List Is Empty """
    if not tasks:
        print("The To-Do List Is Empty.")
        return

    print("Your To-Do List Is As Follows :")
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task}")

def remove_task(tasks: list[str], number: int) -> str | None:
    """ Remove & Return The Task At The Given Task Number Or None If The Number Is Invalid """
    if not (1 <= number <= len(tasks)):
        return None

    return tasks.pop(number - 1)

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Tasks You Want To Add : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 0:
        print("Invalid Input, Please Enter a Non Negative Integer.")
        return

    tasks: list[str] = []

    for i in range(1, n + 1):
        task = input(f"Please Enter Task {i} : ").strip()

        if not task:
            print("Invalid Input, Task Cannot Be Empty.")
            return

        if is_duplicate_task(tasks, task):
            print(f"Invalid Input, Task '{task}' Already Exists In The To-Do List.")
            return

        tasks.append(task)

    while True:
        print()
        print("To-Do List Manager Menu :")
        print("(1) - View Tasks")
        print("(2) - Remove Task")
        print("(3) - Add Task")
        print("(4) - Exit To-Do List Manager")

        choice = input("Please Enter Your Choice (1 To 4) : ").strip()
        print()

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            if not tasks:
                print("The To-Do List Is Empty, There Is Nothing To Remove.")
                continue

            try:
                number = int(input(f"Please Enter The Task Number To Remove (1 To {len(tasks)}) : "))
            except ValueError:
                print("Invalid Input, Please Enter a Valid Task Number.")
                continue

            removed_task = remove_task(tasks, number)

            if removed_task is None:
                print(f"Invalid Input, Task Number Must Be Between 1 & {len(tasks)}.")
            else:
                print(f"Task '{removed_task}' Removed Successfully.")

        elif choice == "3":
            new_task = input("Please Enter The New Task To Add : ").strip()

            if not new_task:
                print("Invalid Input, Task Cannot Be Empty.")
            elif is_duplicate_task(tasks, new_task):
                print(f"Invalid Input, Task '{new_task}' Already Exists In The To-Do List.")
            else:
                tasks.append(new_task)
                print(f"Task '{new_task}' Added Successfully.")

        elif choice == "4":
            print("Program Terminated Successfully.")
            break

        else:
            print("Invalid Choice, Please Enter a Choice Between 1 & 4.")

if __name__ == "__main__":
    main()
