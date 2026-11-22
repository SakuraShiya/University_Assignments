# Write a Python Program To Get a Tuple Of Max & Min From a List Using a Lambda Function.

from collections.abc import Callable

MIN_COUNT: int = 2

max_min: Callable[[list[int]], tuple[int, int]] = lambda numbers: (max(numbers), min(numbers))

def main() -> None:
    try:
        numbers = [int(x) for x in input("Please Enter a Sequence Of Numbers (Separated By Space) : ").split()]
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers.")
        return

    if len(numbers) < MIN_COUNT:
        print(f"Invalid Input, Please Enter At Least {MIN_COUNT} Numbers.")
        return

    result = max_min(numbers)

    print()
    print(f"Tuple Of Maximum & Minimum Is : {result}")
    print(f"Maximum Number Is : {result[0]}")
    print(f"Minimum Number Is : {result[1]}")

if __name__ == "__main__":
    main()
