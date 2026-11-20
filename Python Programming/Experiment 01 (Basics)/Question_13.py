# Write a Python Program To Use Membership Operators To Check If a Given Number Is Present In a List Or Not.

def main() -> None:
    try:
        numbers = [int(x) for x in input("Please Enter The List Elements (Separated By Space) : ").split()]
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers For List Elements.")
        return

    if not numbers:
        print("Invalid Input, The List Cannot Be Empty.")
        return

    try:
        target = int(input("Please Enter a Number To Check Its Presence In The List : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number To Check.")
        return

    print(f"The Given List Is : {numbers}")

    print(f"Is {target} Present In The List? --> {target in numbers}")
    print(f"Is {target} Not Present In The List? --> {target not in numbers}")

if __name__ == "__main__":
    main()
