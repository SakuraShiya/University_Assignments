# Write a Python Program To Find The Nature Of Roots Of a Quadratic Equation Ax² + Bx + C = 0 & Also Find The Roots.

from math import isfinite, sqrt

def solve_quadratic(a: float, b: float, c: float) -> tuple[str, tuple[float, float]]:
    """ Compute The Roots Of a Quadratic Equation Ax² + Bx + C = 0 & Return Their Nature & Values """
    discriminant: float = b**2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + sqrt(discriminant)) / (2 * a) + 0.0
        root2 = (-b - sqrt(discriminant)) / (2 * a) + 0.0
        return "distinct", (root1, root2)
    elif discriminant == 0:
        root = -b / (2 * a) + 0.0
        return "equal", (root, root)
    else:
        real_part = -b / (2 * a) + 0.0
        imaginary_part = sqrt(abs(discriminant)) / abs(2 * a)
        return "complex", (real_part, imaginary_part)

def main() -> None:
    try:
        a = float(input("Please Enter The Coefficient Of x² (A) : "))
        b = float(input("Please Enter The Coefficient Of x (B) : "))
        c = float(input("Please Enter The Constant (C) : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers For Coefficients & Constant.")
        return

    if not (isfinite(a) and isfinite(b) and isfinite(c)):
        print("Invalid Input, Please Enter Finite Numbers For Coefficients & Constant.")
        return

    if a == 0:
        print("Invalid Input, The Coefficient Of x² Cannot Be Zero For a Quadratic Equation.")
        return

    nature, roots = solve_quadratic(a, b, c)

    if nature == "distinct":
        print("The Quadratic Equation Has Two Real & Distinct Roots.")
        print(f"The Roots Are : {roots[0]:.2f} & {roots[1]:.2f}")
    elif nature == "equal":
        print("The Quadratic Equation Has Two Real & Equal Roots.")
        print(f"The Root Is : {roots[0]:.2f}")
    else:
        print("The Quadratic Equation Has Imaginary Roots.")
        print(f"The Roots Are : {roots[0]:.2f} + {roots[1]:.2f}i & {roots[0]:.2f} - {roots[1]:.2f}i")

if __name__ == "__main__":
    main()
