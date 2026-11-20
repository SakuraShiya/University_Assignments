# Write a Python Program To Count & Display The Number Of Capital Letters In a String.

def main() -> None:
    string = input("Please Enter a String : ").strip()

    if not string:
        print("Invalid Input, String Cannot Be Empty.")
        return

    capital_count = sum(1 for char in string if char.isupper())
    print(f"The Number Of Capital Letters In The String Is : {capital_count}")

if __name__ == "__main__":
    main()
