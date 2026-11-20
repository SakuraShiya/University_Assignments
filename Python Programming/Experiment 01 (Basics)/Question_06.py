# Write a Python Program To Calculate Simple Interest.

from math import isfinite

def calculate_simple_interest(principal: float, rate: float, time: float) -> tuple[float, float]:
    """ Calculate Simple Interest & Total Amount Based On The Formula : SI = (P * R * T) / 100 """
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest
    return simple_interest, total_amount

def main() -> None:
    try:
        principal = float(input("Please Enter The Principal Amount : "))
        rate = float(input("Please Enter The Rate Of Interest : "))
        time = float(input("Please Enter The Time (In Years) : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers For Principal, Rate & Time.")
        return

    if not (isfinite(principal) and isfinite(rate) and isfinite(time)):
        print("Invalid Input, Please Enter Finite Numbers For Principal, Rate & Time.")
        return

    if principal <= 0 or rate <= 0 or time <= 0:
        print("Invalid Input, Please Enter Positive Values For Principal, Rate & Time.")
        return

    simple_interest, total_amount = calculate_simple_interest(principal, rate, time)

    if not isfinite(total_amount):
        print("Invalid Input, The Result Is Too Large To Represent.")
        return

    print(f"The Simple Interest Is : {simple_interest:.2f}")
    print(f"The Total Amount Is : {total_amount:.2f}")

if __name__ == "__main__":
    main()
