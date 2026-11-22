# Write a Python Program To Find The Sum Of The Cubes Of All Positive Integers Smaller Than a Given Positive Integer.

def sum_of_cubes(n: int) -> int:
    """ Return The Sum Of The Cubes Of All Positive Integers Smaller Than N """
    total = 0

    for i in range(1, n):
        total += i ** 3

    return total

def main() -> None:
    try:
        n = int(input("Please Enter a Positive Integer : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    print()
    print(f"The Sum Of The Cubes Of All Positive Integers Smaller Than {n} Is : {sum_of_cubes(n)}")

if __name__ == "__main__":
    main()
