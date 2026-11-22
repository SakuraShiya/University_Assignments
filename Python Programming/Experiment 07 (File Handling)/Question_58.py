# Write a Python Program To Store Integers In a File & Find The Maximum, Average & Count Of Numbers Greater Than 100.

from pathlib import Path

NUMBERS_FILE: Path = Path(__file__).with_name("Numbers.txt")
THRESHOLD: int = 100

def main() -> None:
    try:
        numbers = [int(x) for x in input("Please Enter The Integers (Separated By Space) : ").split()]
    except ValueError:
        print("Invalid Input, Please Enter Valid Integers.")
        return

    if not numbers:
        print("Invalid Input, Please Enter At Least One Integer.")
        return

    with open(NUMBERS_FILE, "w", encoding="utf-8") as file:
        for number in numbers:
            file.write(f"{number}\n")

    with open(NUMBERS_FILE, "r", encoding="utf-8") as file:
        stored_numbers = [int(line) for line in file.read().splitlines()]

    average = sum(stored_numbers) / len(stored_numbers)
    above_threshold = sum(1 for number in stored_numbers if number > THRESHOLD)

    print()
    print(f"Numbers Saved To : {NUMBERS_FILE.name}")
    print(f"Maximum Number : {max(stored_numbers)}")
    print(f"Average Of All Numbers : {average:.2f}")
    print(f"Count Of Numbers Greater Than {THRESHOLD} : {above_threshold}")

if __name__ == "__main__":
    main()
