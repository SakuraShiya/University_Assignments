# Write a Python Program To Perform Bitwise Left & Right Shift Operations On a Given Number.

MAX_SHIFT: int = 64

def main() -> None:
    try:
        number = int(input("Please Enter a Number : "))
        bits = int(input("Please Enter The Number Of Bits You Want To Shift : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers.")
        return

    if not (0 <= bits <= MAX_SHIFT):
        print(f"Invalid Input, Please Enter a Shift Value Between 0 & {MAX_SHIFT}.")
        return

    left_shift = number << bits
    right_shift = number >> bits

    print(f"Left Shifted Value Of {number} By {bits} Bits Is : {left_shift}")
    print(f"Right Shifted Value Of {number} By {bits} Bits Is : {right_shift}")

if __name__ == "__main__":
    main()
