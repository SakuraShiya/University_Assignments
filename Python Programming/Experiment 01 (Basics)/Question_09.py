# Write a Python Program To Swap Two Numbers Without Taking Additional Variable.

def main() -> None:
    try:
        a = int(input("Please Enter The First Integer : "))
        b = int(input("Please Enter The Second Integer : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Integers.")
        return

    print(f"Before Swapping First Number Is : {a}")
    print(f"Before Swapping Second Number Is : {b}")

    a, b = b, a

    print(f"After Swapping First Number Is : {a}")
    print(f"After Swapping Second Number Is : {b}")

if __name__ == "__main__":
    main()
