# Write a Python Program To Find The Maximum & Minimum Numbers From a Sequence Of Numbers Using a Function (No Build In Functions).

MIN_COUNT: int = 2

def find_max_min(numbers: list[int]) -> tuple[int, int]:
    """ Find The Maximum & Minimum Numbers In a Single Pass Without Using Built In Max & Min """
    max_num = min_num = numbers[0]

    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return max_num, min_num

def main() -> None:
    try:
        numbers = [int(x) for x in input("Please Enter a Sequence Of Numbers (Separated By Space) : ").split()]
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers.")
        return

    if len(numbers) < MIN_COUNT:
        print(f"Invalid Input, Please Enter At Least {MIN_COUNT} Numbers.")
        return

    max_num, min_num = find_max_min(numbers)

    print()
    if max_num == min_num:
        print(f"All Numbers Are Equal To {max_num}.")
    else:
        print(f"Maximum Number Is : {max_num}")
        print(f"Minimum Number Is : {min_num}")

if __name__ == "__main__":
    main()
