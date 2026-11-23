# Write a Python Program To Use Pandas To Get The Powers Of Array Values Element Wise.

from pandas import DataFrame, Series

COLUMNS: tuple[str, ...] = ("X", "Y", "Z")
MAX_POWER: int = 62
INT64_MAX: int = 2 ** 63 - 1

def read_integers(prompt: str) -> list[int] | None:
    """ Read Space Separated Integers, Or Show An Error & Return None If Any Value Is Invalid """
    try:
        return [int(x) for x in input(prompt).split()]
    except ValueError:
        print("Invalid Input, Please Enter Valid Integers Only.")
        return None

def powers_fit_in_int64(columns: list[list[int]], powers: list[int]) -> bool:
    """ Check That Every Value Raised To Its Row's Power Stays Within The 64 Bit Integer Limit """
    return all(abs(value) ** power <= INT64_MAX for column in columns for value, power in zip(column, powers))

def main() -> None:
    columns: list[list[int]] = []

    for name in COLUMNS:
        values = read_integers(f"Please Enter The Values Of Array {name} (Separated By Space) : ")

        if values is None:
            return

        columns.append(values)

    powers = read_integers("Please Enter The Power For Each Row (Separated By Space) : ")

    if powers is None:
        return

    lengths = {len(column) for column in columns} | {len(powers)}

    if 0 in lengths or len(lengths) != 1:
        print("Invalid Input, All Arrays & The Powers Must Have The Same Non Zero Length.")
        return

    if not all(0 <= power <= MAX_POWER for power in powers):
        print(f"Invalid Input, Each Power Must Be Between 0 & {MAX_POWER}.")
        return

    if not powers_fit_in_int64(columns, powers):
        print("Invalid Input, The Result Is Too Large To Represent.")
        return

    data = DataFrame(dict(zip(COLUMNS, columns)))
    result = data.pow(Series(powers), axis=0)

    print()
    print("The Given DataFrame Is :")
    print(data)

    print()
    print(f"The Power For Each Row Is : {', '.join(str(power) for power in powers)}")

    print()
    print("The DataFrame After Raising Each Row To Its Power Is :")
    print(result)

if __name__ == "__main__":
    main()
