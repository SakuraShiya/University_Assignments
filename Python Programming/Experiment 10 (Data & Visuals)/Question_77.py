# Write a Python Program To Use Pandas To Get The First 3 Rows Of a Given Data Frame.

from pandas import DataFrame

ROW_COUNT: int = 3

def main() -> None:
    data = DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, 35, 40, 45],
        "Marks": [85, 90, 95, 80, 75],
        "Attempts": [1, 2, 3, 4, 5],
    })

    print("The Given DataFrame Is :")
    print(data)

    print()
    print(f"The First {ROW_COUNT} Rows Of The DataFrame Are :")
    print(data.head(ROW_COUNT))

if __name__ == "__main__":
    main()
