# Write a Python Program To Find The Volume Of a Cone Using a Lambda Function.

from collections.abc import Callable
from math import isfinite, pi

cone_volume: Callable[[float, float], float] = lambda radius, height: pi * radius ** 2 * height / 3

def main() -> None:
    try:
        radius = float(input("Please Enter The Radius Of The Cone : "))
        height = float(input("Please Enter The Height Of The Cone : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers For Radius & Height.")
        return

    if not (isfinite(radius) and isfinite(height)) or radius <= 0 or height <= 0:
        print("Invalid Input, Please Enter Finite Positive Values For Radius & Height.")
        return

    volume = cone_volume(radius, height)

    if not isfinite(volume):
        print("Invalid Input, The Result Is Too Large To Represent.")
        return

    print()
    print(f"The Volume Of The Cone Is : {volume:.2f}")

if __name__ == "__main__":
    main()
