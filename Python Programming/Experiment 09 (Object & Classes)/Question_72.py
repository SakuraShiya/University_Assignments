# Write a Python Program To Create a Class For Operator Overloading Which Adds Two Point Objects Where Point Has X & Y Values.

from math import isfinite

class Point:
    """ Store a Point With X & Y Values That Supports Adding Two Points With The + Operator """

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: object) -> Point:
        """ Add Two Points By Adding Their X Values & Their Y Values Separately """
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)

        return NotImplemented

    def __str__(self) -> str:
        """ Show The Point As Point(X, Y) Without Unnecessary Decimal Places """
        return f"Point({self.x + 0.0:.15g}, {self.y + 0.0:.15g})"

def main() -> None:
    try:
        x1, y1 = map(float, input("Please Enter X & Y For Point 1 (Separated By Space) : ").split())
        x2, y2 = map(float, input("Please Enter X & Y For Point 2 (Separated By Space) : ").split())
    except ValueError:
        print("Invalid Input, Please Enter Exactly Two Numbers For Each Point.")
        return

    if not all(isfinite(value) for value in (x1, y1, x2, y2)):
        print("Invalid Input, Please Enter Finite Numbers Only.")
        return

    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    result = point1 + point2

    if not (isfinite(result.x) and isfinite(result.y)):
        print("Invalid Input, The Result Is Too Large To Represent.")
        return

    print()
    print(f"Point 1 : {point1}")
    print(f"Point 2 : {point2}")
    print(f"{point1} + {point2} = {result}")

if __name__ == "__main__":
    main()
