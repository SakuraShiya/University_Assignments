# Write a Python Program To Create a Contact Book Where Users Can Store, Search, Update & Delete Contacts (Use Dictionary).

PHONE_LENGTH: int = 10

def is_valid_phone(phone_number: str) -> bool:
    """ Check Whether The Phone Number Contains Exactly 10 Digits """
    return phone_number.isdecimal() and len(phone_number) == PHONE_LENGTH

def get_contact_error(contacts: dict[str, str], name: str, phone_number: str) -> str | None:
    """ Return The Error Message For an Invalid Or Duplicate Contact, Otherwise None """
    if not name:
        return "Invalid Input, Contact Name Cannot Be Empty."
    if not is_valid_phone(phone_number):
        return f"Invalid Input, Phone Number Must Contain Exactly {PHONE_LENGTH} Digits."
    if name in contacts:
        return f"Invalid Input, Contact '{name}' Already Exists."
    return None

def display_contacts(contacts: dict[str, str]) -> None:
    """ Display All Contacts Sorted By Name Or a Message If The Contact Book Is Empty """
    if not contacts:
        print("The Contact Book Is Empty.")
        return

    print("All Existing Contacts Are As Follows :")
    for name in sorted(contacts):
        print(f"{name} - {contacts[name]}")

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Contacts You Want To Add : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 0:
        print("Invalid Input, Please Enter a Non Negative Integer.")
        return

    contacts: dict[str, str] = {}

    for i in range(1, n + 1):
        name = input(f"Please Enter The Name Of Contact {i} : ").strip().title()
        phone_number = input(f"Please Enter The Phone Number Of Contact {i} : ").strip()

        error = get_contact_error(contacts, name, phone_number)

        if error:
            print(error)
            return

        contacts[name] = phone_number

    while True:
        print()
        print("Phone Contact Book Menu :")
        print("(1) - Add Contact")
        print("(2) - Search Contact")
        print("(3) - Update Contact")
        print("(4) - Delete Contact")
        print("(5) - Display All Contacts")
        print("(6) - Exit Contact Book")

        choice = input("Please Enter Your Choice (1 To 6) : ").strip()
        print()

        if choice == "1":
            name = input("Please Enter The Name Of The New Contact : ").strip().title()
            phone_number = input("Please Enter The Phone Number Of The New Contact : ").strip()

            error = get_contact_error(contacts, name, phone_number)

            if error:
                print(error)
            else:
                contacts[name] = phone_number
                print(f"Contact '{name}' Added Successfully.")

        elif choice == "2":
            name = input("Please Enter The Name Of The Contact To Search : ").strip().title()

            if name in contacts:
                print(f"Contact Found : {name} - {contacts[name]}")
            else:
                print("Contact Not Found.")

        elif choice == "3":
            name = input("Please Enter The Name Of The Contact To Update : ").strip().title()

            if name not in contacts:
                print("Contact Not Found.")
                continue

            phone_number = input("Please Enter The New Phone Number : ").strip()

            if is_valid_phone(phone_number):
                contacts[name] = phone_number
                print("Contact Updated Successfully.")
            else:
                print(f"Invalid Input, Phone Number Must Contain Exactly {PHONE_LENGTH} Digits.")

        elif choice == "4":
            name = input("Please Enter The Name Of The Contact To Delete : ").strip().title()

            if name in contacts:
                del contacts[name]
                print("Contact Deleted Successfully.")
            else:
                print("Contact Not Found.")

        elif choice == "5":
            display_contacts(contacts)

        elif choice == "6":
            print("Program Terminated Successfully.")
            break

        else:
            print("Invalid Choice, Please Enter a Choice Between 1 & 6.")

if __name__ == "__main__":
    main()
