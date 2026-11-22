# Write a Python Program To Print 1 To N Using a Recursive Function (Note - Do Not Use Loop).

MAX_N: int = 900

def print_numbers(n: int) -> None:
    """ Print The Numbers From 1 To N Separated By Commas Using Recursion """
    if n == 0:
        return

    print_numbers(n - 1)
    print(n if n == 1 else f", {n}", end="")

def main() -> None:
    try:
        n = int(input("Please Enter a Number To Display From 1 To N : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if not (1 <= n <= MAX_N):
        print(f"Invalid Input, Please Enter a Number Between 1 & {MAX_N} (Recursion Depth Limit).")
        return

    print()
    print(f"Numbers From 1 To {n} Are : ", end="")
    print_numbers(n)
    print()

if __name__ == "__main__":
    main()
