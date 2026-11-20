# Write a Python Program To Check Whether a Given Number Is a Palindrome Or Not.

def is_palindrome(num: int) -> bool:
    """ Check Whether The Given Number Is a Palindrome """
    if num < 0:
        return False

    original = num
    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10

    return original == rev

def main() -> None:
    try:
        a = int(input("Please Enter a Number : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if a < 0:
        print("Invalid Input, Please Enter a Non Negative Integer.")
        return

    if is_palindrome(a):
        print(f"{a} Is a Palindrome Number.")
    else:
        print(f"{a} Is Not a Palindrome Number.")

if __name__ == "__main__":
    main()
