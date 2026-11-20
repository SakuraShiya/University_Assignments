# Write a Python Program To Input 2 Sets Of Fruits & Perform All The Set Operations.

def perform_set_operations(set1: set[str], set2: set[str]) -> dict[str, set[str] | bool]:
    """ Perform All The Set Operations On The Two Given Sets """
    return {
        "Union Of The Two Sets Is": set1.union(set2),
        "Intersection Of The Two Sets Is": set1.intersection(set2),
        "Difference Of Set 1 From Set 2 Is": set1.difference(set2),
        "Difference Of Set 2 From Set 1 Is": set2.difference(set1),
        "Symmetric Difference Of The Two Sets Is": set1.symmetric_difference(set2),
        "Is Set 1 a Subset Of Set 2": set1.issubset(set2),
        "Is Set 1 a Superset Of Set 2": set1.issuperset(set2),
        "Are The Two Sets Disjoint": set1.isdisjoint(set2),
    }

def format_set(fruits: set[str]) -> str:
    """ Return The Set As Sorted Comma Separated Text Or Empty Set """
    return ", ".join(sorted(fruits)) if fruits else "Empty Set"

def main() -> None:
    fruits1 = input("Please Enter The First Set Of Fruits : ").strip()
    fruits2 = input("Please Enter The Second Set Of Fruits : ").strip()

    if not fruits1 or not fruits2:
        print("Invalid Input, Sets Cannot Be Empty.")
        return

    set1 = set(fruits1.split())
    set2 = set(fruits2.split())

    print(f"The First Set Of Fruits Is : {format_set(set1)}")
    print(f"The Second Set Of Fruits Is : {format_set(set2)}")

    operations = perform_set_operations(set1, set2)

    for description, result in operations.items():
        value = result if isinstance(result, bool) else format_set(result)
        print(f"{description} : {value}")

if __name__ == "__main__":
    main()
