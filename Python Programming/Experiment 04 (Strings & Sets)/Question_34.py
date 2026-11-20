# Write a Python Program To Count The Number Of Vowels In a String.

VOWELS: str = "aeiouAEIOU"

def main() -> None:
    string = input("Please Enter a String : ").strip()

    if not string:
        print("Invalid Input, String Cannot Be Empty.")
        return

    vowel_count = sum(1 for char in string if char in VOWELS)
    print(f"The Number Of Vowels In The String Is : {vowel_count}")

if __name__ == "__main__":
    main()
