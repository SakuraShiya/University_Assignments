# Write a Python Program To Create a Counter That Shows How Many Times The Program Has Been Executed.

from pathlib import Path

COUNTER_FILE: Path = Path(__file__).with_name("Counter.txt")

def main() -> None:
    try:
        with open(COUNTER_FILE, "r", encoding="utf-8") as file:
            count = int(file.read())

        if count < 0:
            raise ValueError("The Count Cannot Be Negative")
    except FileNotFoundError:
        count = 0
    except ValueError:
        print("Warning, The Counter File Was Corrupted, So The Count Has Been Reset.")
        count = 0

    count += 1

    with open(COUNTER_FILE, "w", encoding="utf-8") as file:
        file.write(str(count))

    print(f"This Program Has Been Executed {count} {'Time' if count == 1 else 'Times'}.")

if __name__ == "__main__":
    main()
