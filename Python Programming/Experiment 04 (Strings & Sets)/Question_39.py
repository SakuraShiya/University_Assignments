# Write a Python Program To Input 2 Sets Of Fruits & Perform Basic Set Operations.

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

    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set = set1.difference(set2)
    symmetric_difference_set = set1.symmetric_difference(set2)

    print(f"Union Of The Two Sets Is : {format_set(union_set)}")
    print(f"Intersection Of The Two Sets Is : {format_set(intersection_set)}")
    print(f"Difference Of Set 1 From Set 2 Is : {format_set(difference_set)}")
    print(f"Symmetric Difference Of The Two Sets Is : {format_set(symmetric_difference_set)}")

if __name__ == "__main__":
    main()
