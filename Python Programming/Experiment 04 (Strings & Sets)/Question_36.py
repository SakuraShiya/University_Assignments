# Write a Python Program To Input a String & a Sub String To Display Total Occurrences Traversing From Left To Right.

def count_occurrences(string: str, substring: str) -> int:
    """ Count The Overlapping Occurrences Of a Sub String In a String From Left To Right """
    if not substring:
        return 0

    last_start = len(string) - len(substring)

    return sum(1 for i in range(last_start + 1) if string.startswith(substring, i))

def main() -> None:
    string = input("Please Enter a String : ").strip()
    substring = input("Please Enter a Sub String : ").strip()

    if not string or not substring:
        print("Invalid Input, String Or Sub String Cannot Be Empty.")
        return

    occurrence_count = count_occurrences(string, substring)
    print(f"The Total Occurrences Of The Sub String In The String Is : {occurrence_count}")

if __name__ == "__main__":
    main()
