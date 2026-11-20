# Write a Python Program To Print Fibonacci Series.

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Terms In Fibonacci Series : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n <= 0:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    a, b = 0, 1

    print(f"Fibonacci Series Up To {n} Terms Is : ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

if __name__ == "__main__":
    main()
