# Write a Python Program To Print The Truth Table For The Given Bitwise Operator.

from collections.abc import Callable

BINARY_OPERATORS: dict[str, Callable[[int, int], int]] = {
    "&": lambda a, b: a & b,
    "|": lambda a, b: a | b,
    "^": lambda a, b: a ^ b,
}

VALID_OPERATORS: tuple[str, ...] = (*BINARY_OPERATORS, "~")

def print_truth_table(symbol: str) -> None:
    """ Print The Truth Table For The Given Bitwise Operator Using Dictionary Dispatch & Bit Masking """
    print(f"Truth Table For '{symbol}' Operator")

    if symbol == "~":
        print("----------")
        print("A | Result")
        for a in (0, 1):
            result = ~a & 1
            print(f"{a} | {result}")
        print("----------")
    else:
        operation = BINARY_OPERATORS[symbol]
        print("------------")
        print("A B | Result")
        for a in (0, 1):
            for b in (0, 1):
                result = operation(a, b)
                print(f"{a} {b} | {result}")
        print("------------")

def main() -> None:
    symbol = input(f"Please Enter a Bitwise Operator ({', '.join(VALID_OPERATORS)}) : ").strip()

    if symbol not in VALID_OPERATORS:
        print("Invalid Input, Please Enter a Valid Bitwise Operator.")
        return

    print_truth_table(symbol)

if __name__ == "__main__":
    main()
