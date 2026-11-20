# Write a Python Program To Print a Symmetrical Number & Star Pattern For a Given Number Of Rows.

def print_pattern(n: int) -> None:
    """ Print a Symmetrical Number & Star Pattern For a Given Number Of Rows """
    if n < 1:
        return

    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end="")

        stars = n - i
        print(" " * stars + " ".join("*" * stars) + " " * stars, end="")

        start_num = i - 1 if i == n else i
        for k in range(start_num, 0, -1):
            print(k, end="")
        print()

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Rows : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    print_pattern(n)

if __name__ == "__main__":
    main()
