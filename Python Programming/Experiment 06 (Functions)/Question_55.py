# Write a Python Program To Check Whether All The Values In a Dictionary Are Same Or Not Using a Lambda Function.

from collections.abc import Callable

all_values_same: Callable[[dict[str, str]], bool] = lambda data: len(set(data.values())) == 1

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Key Value Pairs : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    data: dict[str, str] = {}

    for i in range(1, n + 1):
        key = input(f"Please Enter Key {i} : ").strip()

        if not key:
            print("Invalid Input, Key Cannot Be Empty.")
            return

        if key in data:
            print(f"Invalid Input, Key '{key}' Has Already Been Entered.")
            return

        value = input(f"Please Enter The Value For Key '{key}' : ").strip()

        if not value:
            print("Invalid Input, Value Cannot Be Empty.")
            return

        data[key] = value

    print()
    print(f"The Given Dictionary Is : {data}")

    if all_values_same(data):
        print("All The Values In The Dictionary Are Same.")
    else:
        print("All The Values In The Dictionary Are Not Same.")

if __name__ == "__main__":
    main()
