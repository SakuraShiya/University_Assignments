# Write a Python Program To Scan N Values In Range Of 0 To 3 & Print The Number Of Times Each Value Has Occurred.

MIN_VALUE: int = 0
MAX_VALUE: int = 3

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Values : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    count = {value: 0 for value in range(MIN_VALUE, MAX_VALUE + 1)}

    for i in range(1, n + 1):
        try:
            num = int(input(f"Please Enter Value {i} (Between {MIN_VALUE} & {MAX_VALUE}) : "))
        except ValueError:
            print("Invalid Input, Please Enter a Valid Number.")
            return

        if not (MIN_VALUE <= num <= MAX_VALUE):
            print(f"Invalid Input, Value Must Be Between {MIN_VALUE} & {MAX_VALUE}.")
            return

        count[num] += 1

    print()
    for value, occurrences in count.items():
        if occurrences > 0:
            print(f"Value {value} Has Occurred {occurrences} {'Time' if occurrences == 1 else 'Times'}")

if __name__ == "__main__":
    main()
