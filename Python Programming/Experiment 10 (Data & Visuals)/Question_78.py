# Write a Python Program To Use Pandas To Find & Replace The Missing Values In a Given Data Frame.

from pandas import DataFrame

def main() -> None:
    data = DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Age": [25, 30, 35, 40, 45],
        "Marks": [85, None, 95, 60, 75],
        "Attempts": [1, 2, 3, None, 5],
    })

    print("The DataFrame Before Replacing Missing Values Is :")
    print(data)

    print()
    print("Number Of Missing Values In Each Column :")
    print(data.isna().sum().to_string())

    marks_mean = round(data["Marks"].mean())
    attempts_median = round(data["Attempts"].median())

    data["Marks"] = data["Marks"].fillna(marks_mean).astype(int)
    data["Attempts"] = data["Attempts"].fillna(attempts_median).astype(int)

    print()
    print(f"Missing Marks Replaced With The Mean ({marks_mean}) & Missing Attempts Replaced With The Median ({attempts_median}).")

    print()
    print("The DataFrame After Replacing Missing Values Is :")
    print(data)

if __name__ == "__main__":
    main()
