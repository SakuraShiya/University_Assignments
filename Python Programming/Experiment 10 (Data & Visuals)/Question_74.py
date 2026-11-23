# Write a Python Program To Create a 3x3 NumPy Array & Find The Sum Of Each Row & Column & The Second Maximum Element.

from numpy import array, unique

SIZE: int = 3

def main() -> None:
    try:
        numbers = [int(x) for x in input(f"Please Enter {SIZE * SIZE} Numbers For The {SIZE}x{SIZE} Array (Separated By Space) : ").split()]
    except ValueError:
        print("Invalid Input, Please Enter Valid Integers.")
        return

    if len(numbers) != SIZE * SIZE:
        print(f"Invalid Input, Please Enter Exactly {SIZE * SIZE} Numbers ({len(numbers)} Were Entered).")
        return

    matrix = array(numbers).reshape(SIZE, SIZE)
    distinct_values = unique(matrix)

    print()
    print("The Given Array Is :")
    print(matrix)

    print()
    print(f"Sum Of Each Row : {matrix.sum(axis=1)}")
    print(f"Sum Of Each Column : {matrix.sum(axis=0)}")

    if len(distinct_values) < 2:
        print("There Is No Second Maximum Element As All Elements Are The Same.")
    else:
        print(f"The Second Maximum Element In The Array Is : {distinct_values[-2]}")

if __name__ == "__main__":
    main()
