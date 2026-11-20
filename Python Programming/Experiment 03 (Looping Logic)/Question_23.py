# Write a Python Program To Check Whether The Given Number Is an Armstrong Number Or Not.

def is_armstrong_number(num: int) -> bool:
    """ Check Whether The Given Number Is an Armstrong Number """
    if num < 0:
        return False

    count = len(str(num))
    total = 0
    original = num

    while num > 0:
        digit = num % 10
        total += digit ** count
        num //= 10

    return original == total

def main() -> None:
    try:
        a = int(input("Please Enter a Number : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if a < 0:
        print("Invalid Input, Armstrong Number Is Not Defined For Negative Numbers.")
        return

    if is_armstrong_number(a):
        print(f"{a} Is an Armstrong Number.")
    else:
        print(f"{a} Is Not an Armstrong Number.")

if __name__ == "__main__":
    main()
