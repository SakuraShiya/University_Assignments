# Write a Python Program To Create a NumPy Array & Find The Sum Of All Elements In The Array.

from numpy import array

def main() -> None:
    try:
        numbers = [int(x) for x in input("Please Enter The Numbers Of The Array (Separated By Space) : ").split()]
    except ValueError:
        print("Invalid Input, Please Enter Valid Integers.")
        return

    if not numbers:
        print("Invalid Input, Please Enter At Least One Number.")
        return

    values = array(numbers)

    print()
    print(f"The Given Array Is : {values}")
    print(f"The Sum Of All Elements In The Array Is : {values.sum()}")

if __name__ == "__main__":
    main()
