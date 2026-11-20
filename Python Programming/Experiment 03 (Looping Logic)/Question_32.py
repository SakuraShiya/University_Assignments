# Write a Python Program To Print The Sum Of The Following Series (1 + 1/2 + 1/3 + 1/4 ... N Terms).

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Terms : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    total = 0.0

    for i in range(1, n + 1):
        total += 1 / i

    print(f"The Sum Of The Series Up To {n} Terms Is : {total:.4f}")

if __name__ == "__main__":
    main()
