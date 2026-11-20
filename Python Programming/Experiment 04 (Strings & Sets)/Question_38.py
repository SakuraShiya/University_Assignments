# Write a Python Program To Count Number Of Unique Words In a Given Sentence Using Sets.

def main() -> None:
    sentence = input("Please Enter a Sentence : ").strip()

    if not sentence:
        print("Invalid Input, Sentence Cannot Be Empty.")
        return

    unique_count = len(set(sentence.lower().split()))
    print(f"The Number Of Unique Words In The Sentence Is : {unique_count}")

if __name__ == "__main__":
    main()
