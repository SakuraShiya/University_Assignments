# Write a Python Program To Print Sum Of Digits.

def main() -> None:
    try:
        a = int(input("Please Enter a Number : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if a < 0:
        print("Invalid Input, Please Enter a Non Negative Integer.")
        return

    original = a
    total = 0

    while a > 0:
        digit = a % 10
        total += digit
        a //= 10

    print(f"The Sum Of Digits Of {original} Is : {total}")

if __name__ == "__main__":
    main()
