# Write a Python Program To Find If a Given Number Is a Prime Number Or Not.

from math import isqrt

def is_prime(num: int) -> bool:
    """ Check Whether a Given Number Is Prime Or Not """
    if num <= 1:
        return False

    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False

    return True

def main() -> None:
    try:
        a = int(input("Please Enter a Number : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if a < 0:
        print("Invalid Input, Please Enter a Non Negative Integer.")
        return

    if is_prime(a):
        print(f"{a} Is a Prime Number.")
    else:
        print(f"{a} Is Not a Prime Number.")

if __name__ == "__main__":
    main()
