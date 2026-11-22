# Write a Python Program To Print Fibonacci Series Using a Recursive Function.

MAX_TERMS: int = 500

def fibonacci_series(n: int) -> list[int]:
    """ Return The First N Terms Of The Fibonacci Series Using Recursion """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci_series(n - 1)
        series.append(series[-1] + series[-2])
        return series

def format_series(series: list[int]) -> str:
    """ Return The Series As Comma Separated Text """
    return ", ".join(str(term) for term in series)

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Terms In Fibonacci Series : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if not (1 <= n <= MAX_TERMS):
        print(f"Invalid Input, Please Enter a Number Of Terms Between 1 & {MAX_TERMS} (Recursion Depth Limit).")
        return

    series = fibonacci_series(n)

    print()
    print(f"Fibonacci Series Up To {n} {'Term' if n == 1 else 'Terms'} Is : {format_series(series)}")

if __name__ == "__main__":
    main()
