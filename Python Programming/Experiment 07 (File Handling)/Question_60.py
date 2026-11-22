# Write a Python Program To Perform Integer Division For N Test Cases Of A & B & Handle Errors Like Division By Zero & Invalid Input.

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Test Cases : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    for i in range(1, n + 1):
        print()

        try:
            a, b = map(int, input(f"Please Enter Test Case {i} (A B) : ").split())
            print(f"The Result Of {a} Divided By {b} Is : {a // b}")
        except ValueError:
            print("Invalid Input, Please Enter Exactly Two Integers Separated By Space.")
        except ZeroDivisionError:
            print("Invalid Input, Division By Zero Is Not Allowed.")

if __name__ == "__main__":
    main()
