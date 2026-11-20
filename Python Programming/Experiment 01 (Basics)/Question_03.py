# Write a Python Program To Input Different Data Types From User & Print Them.

def main() -> None:
    try:
        int_value = int(input("Please Enter an Integer Value : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Integer.")
        return

    try:
        float_value = float(input("Please Enter a Floating Point Value : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Floating Point Number.")
        return

    raw_bool = input("Please Enter a Boolean Value (True/False) : ").strip().lower()

    if raw_bool not in ("true", "false"):
        print("Invalid Input, Please Enter True Or False.")
        return

    bool_value = raw_bool == "true"

    str_value = input("Please Enter a String Value : ").strip()

    if not str_value:
        print("Invalid Input, String Value Cannot Be Empty.")
        return

    print(f"Integer Value : {int_value}")
    print(f"Floating Point Value : {float_value}")
    print(f"Boolean Value : {bool_value}")
    print(f"String Value : {str_value}")

if __name__ == "__main__":
    main()
