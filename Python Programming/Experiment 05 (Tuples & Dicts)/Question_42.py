# Write a Python Program To Create a Tuple & Store N Numeric Values & Find Average Of All Values.

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Values To Be Stored In Tuple : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    values: tuple[int, ...] = ()

    for i in range(1, n + 1):
        try:
            value = int(input(f"Please Enter Value {i} : "))
        except ValueError:
            print("Invalid Input, Please Enter a Valid Number.")
            return

        values += (value,)

    average = sum(values) / len(values)

    print()
    print(f"The Given Tuple Is : {values}")
    print(f"The Average Of All Values In The Tuple Is : {average:.2f}")

if __name__ == "__main__":
    main()
