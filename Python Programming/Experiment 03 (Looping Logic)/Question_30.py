# Write a Python Program To Print The Multiplication Table Of a Given Number Using Loop.

def main() -> None:
    try:
        a = int(input("Please Enter a Number To Print Its Multiplication Table : "))
        n = int(input("Please Enter The Range Up To Which You Want The Multiplication Table : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers.")
        return

    if a < 0:
        print("Invalid Input, Please Enter a Non Negative Integer.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    for i in range(1, n + 1):
        print(f"{a} x {i} = {a * i}")

if __name__ == "__main__":
    main()
