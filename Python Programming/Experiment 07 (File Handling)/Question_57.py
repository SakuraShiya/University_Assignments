# Write a Python Program To Add Names To a File & Count All Names, Names Starting With a Vowel & Find The Longest Name.

from pathlib import Path

NAMES_FILE: Path = Path(__file__).with_name("Names.txt")
VOWELS: str = "AEIOU"

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Names To Add : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    names: list[str] = []

    for i in range(1, n + 1):
        name = input(f"Please Enter Name {i} : ").strip()

        if not name:
            print("Invalid Input, Name Cannot Be Empty.")
            return

        names.append(name)

    with open(NAMES_FILE, "w", encoding="utf-8") as file:
        for name in names:
            file.write(name + "\n")

    with open(NAMES_FILE, "r", encoding="utf-8") as file:
        stored_names = file.read().splitlines()

    vowel_names = [name for name in stored_names if name[0].upper() in VOWELS]
    longest_name = max(stored_names, key=len)

    print()
    print(f"Names Saved To : {NAMES_FILE.name}")
    print(f"Total Names In The File : {len(stored_names)}")
    print(f"Names Starting With a Vowel : {len(vowel_names)} ({', '.join(vowel_names) if vowel_names else 'None'})")
    print(f"Longest Name : {longest_name}")

if __name__ == "__main__":
    main()
