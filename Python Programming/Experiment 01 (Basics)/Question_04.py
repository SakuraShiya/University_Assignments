# Write a Python Program To Perform Basic Arithmetic Operations On Two Numbers.

def main() -> None:
    try:
        a = int(input("Please Enter The First Integer : "))
        b = int(input("Please Enter The Second Integer : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Integers.")
        return

    print(f"The Addition Of {a} & {b} Is : {a + b}")
    print(f"The Subtraction Of {a} & {b} Is : {a - b}")
    print(f"The Multiplication Of {a} & {b} Is : {a * b}")

    if b != 0:
        print(f"The Division Of {a} & {b} Is : {a / b:.2f}")
        print(f"The Quotient & Remainder Of {a} & {b} Are : {a // b} & {a % b}")
    else:
        print("Division & Modulus By Zero Are Not Allowed.")

if __name__ == "__main__":
    main()
