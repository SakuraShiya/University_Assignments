# Write a Python Program To Compute The Length Of The Hypotenuse Of a Right Triangle Using Pythagoras Theorem.

from math import hypot, isfinite

def calculate_hypotenuse(base: float, perpendicular: float) -> float:
    """ Return The Hypotenuse Given Two Positive Side Lengths Of a Right Triangle Using Pythagoras Theorem (Overflow Safe) """
    return hypot(base, perpendicular)

def main() -> None:
    try:
        base = float(input("Please Enter Length Of The Base : "))
        perpendicular = float(input("Please Enter Length Of The Perpendicular : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers For Length Of Sides.")
        return

    if not (isfinite(base) and isfinite(perpendicular)) or base <= 0 or perpendicular <= 0:
        print("Invalid Input, Please Enter Finite Positive Numbers Only.")
        return

    hypotenuse = calculate_hypotenuse(base, perpendicular)

    if not isfinite(hypotenuse):
        print("Invalid Input, The Result Is Too Large To Represent.")
        return

    print(f"The Length Of The Hypotenuse Is : {hypotenuse:.2f}")

if __name__ == "__main__":
    main()
