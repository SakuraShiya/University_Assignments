# Write a Python Program To Count The Total Numbers Divisible By A Or B Between 1 To N.

def main() -> None:
    try:
        a = int(input("Please Enter The First Number : "))
        b = int(input("Please Enter The Second Number : "))
        n = int(input("Please Enter The Upper Limit For Counting Divisible Numbers : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers.")
        return

    if any(x < 1 for x in [a, b, n]):
        print("Invalid Input, Please Enter Positive Integers.")
        return

    count = 0

    for i in range(1, n + 1):
        if i % a == 0 or i % b == 0:
            count += 1

    print(f"Total Count Of Numbers Divisible By {a} Or {b} Between 1 To {n} Is : {count}")

if __name__ == "__main__":
    main()
