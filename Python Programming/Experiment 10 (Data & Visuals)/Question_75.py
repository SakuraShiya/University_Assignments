# Write a Python Program To Perform Matrix Multiplication Of Any 2 N x N Matrices Using NumPy.

from numpy import array

MAX_SIZE: int = 10
INT64_MAX: int = 2 ** 63 - 1

def read_matrix_values(label: str, n: int) -> list[int] | None:
    """ Read Exactly N x N Integers For One Matrix, Or Show An Error & Return None """
    try:
        values = [int(x) for x in input(f"Please Enter The {n * n} Elements Of The {label} Matrix (Separated By Space) : ").split()]
    except ValueError:
        print(f"Invalid Input, Please Enter Valid Integers For The {label} Matrix.")
        return None

    if len(values) != n * n:
        print(f"Invalid Input, The {label} Matrix Needs Exactly {n * n} Elements ({len(values)} Were Entered).")
        return None

    return values

def product_fits_in_int64(first: list[int], second: list[int], n: int) -> bool:
    """ Check That Even The Largest Possible Element Of The Product Stays Within The 64 Bit Integer Limit """
    return max(abs(value) for value in first) * max(abs(value) for value in second) * n <= INT64_MAX

def main() -> None:
    try:
        n = int(input("Please Enter The Size Of The Square Matrices (N For N x N) : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if not (1 <= n <= MAX_SIZE):
        print(f"Invalid Input, Please Enter a Size Between 1 & {MAX_SIZE}.")
        return

    first_values = read_matrix_values("First", n)

    if first_values is None:
        return

    second_values = read_matrix_values("Second", n)

    if second_values is None:
        return

    if not product_fits_in_int64(first_values, second_values, n):
        print("Invalid Input, The Result Is Too Large To Represent.")
        return

    first_matrix = array(first_values).reshape(n, n)
    second_matrix = array(second_values).reshape(n, n)
    result = first_matrix @ second_matrix

    print()
    print("First Matrix :")
    print(first_matrix)

    print()
    print("Second Matrix :")
    print(second_matrix)

    print()
    print("Result Of Matrix Multiplication :")
    print(result)

if __name__ == "__main__":
    main()
