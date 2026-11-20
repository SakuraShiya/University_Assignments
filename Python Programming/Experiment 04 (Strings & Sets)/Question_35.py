# Write a Python Program To Input a Sentence & Print Words In Separate Lines.

def main() -> None:
    sentence = input("Please Enter a Sentence : ").strip()

    if not sentence:
        print("Invalid Input, Sentence Cannot Be Empty.")
        return

    words = sentence.split()

    print("The Words In The Sentence Are :")
    for word in words:
        print(word)

if __name__ == "__main__":
    main()
