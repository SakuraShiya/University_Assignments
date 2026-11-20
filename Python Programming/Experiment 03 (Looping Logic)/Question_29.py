# Write a Python Program To Convert All Lower Cases To Upper Case In a String.

def main() -> None:
    string = input("Please Enter a String : ").strip()

    if not string:
        print("Invalid Input, String Cannot Be Empty.")
        return

    upper_case_string = string.upper()
    print(f"The String After Converting All Lower Cases To Upper Case Is : {upper_case_string}")

if __name__ == "__main__":
    main()
