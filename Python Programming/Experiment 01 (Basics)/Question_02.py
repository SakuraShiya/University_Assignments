# Write a Python Program To Take a String Input From User & Print It.

def main() -> None:
    text = input("Please Enter a String : ").strip()

    if not text:
        print("Invalid Input, String Value Cannot Be Empty.")
        return

    print(f"String Value : {text}")

if __name__ == "__main__":
    main()
