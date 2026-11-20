# Write a Python Program To Count The Number Of Occurrences Of Each Alphabet In a Given String.

LOWERCASE_ALPHABET: str = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE_ALPHABET: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def count_alphabet_occurrences(string: str) -> dict[str, int]:
    """ Count The Occurrences Of Each Lowercase & Uppercase Alphabet In The Given String """
    alphabet_count = {char: 0 for char in LOWERCASE_ALPHABET + UPPERCASE_ALPHABET}

    for char in string:
        if char in alphabet_count:
            alphabet_count[char] += 1

    return {char: count for char, count in alphabet_count.items() if count > 0}

def main() -> None:
    string = input("Please Enter a String : ").strip()

    if not string:
        print("Invalid Input, String Cannot Be Empty.")
        return

    occurrences = count_alphabet_occurrences(string)

    if not occurrences:
        print("Invalid Input, No Alphabets Found In The String.")
        return

    print("The Number Of Occurrences Of Each Alphabet In The String Is :")
    for char, count in occurrences.items():
        print(f"{char} : {count}")

if __name__ == "__main__":
    main()
