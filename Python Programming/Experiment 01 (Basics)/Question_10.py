# Write a Python Program To Find Sum Of First N Natural Numbers.

def sum_of_natural_numbers(n: int) -> int:
    """ Calculate The Sum Of The First N Natural Numbers Using Gauss's Formula """
    return n * (n + 1) // 2

def main() -> None:
    try:
        n = int(input("Please Enter a Number (To Get Sum Of First N Natural Numbers) : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Number.")
        return

    total = sum_of_natural_numbers(n)

    try:
        print(f"The Sum Of First {n} Natural Numbers Is : {total}")
    except ValueError:
        print("Invalid Input, The Result Is Too Large To Display.")

if __name__ == "__main__":
    main()
