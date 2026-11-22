# Write a Python Program To Create 2 Lists & Generate a Dictionary With Keys From First List & Values From Second List.

def has_duplicates(items: list[int]) -> bool:
    """ Check Whether The List Contains Any Repeated Item """
    return len(set(items)) != len(items)

def create_dict_from_lists(keys: list[int], values: list[int]) -> dict[int, int]:
    """ Pair Each Key With The Value At The Same Position Using Zip """
    return dict(zip(keys, values))

def main() -> None:
    try:
        keys = [int(x) for x in input("Please Enter The Keys (Separated By Space) : ").split()]
        values = [int(x) for x in input("Please Enter The Values (Separated By Space) : ").split()]
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers For Keys & Values.")
        return

    if not keys or not values:
        print("Invalid Input, Keys & Values Cannot Be Empty.")
        return

    if len(keys) != len(values):
        print(f"Invalid Input, {len(keys)} Keys & {len(values)} Values Were Entered, Both Lists Must Be Of Equal Length.")
        return

    if has_duplicates(keys):
        print("Invalid Input, Keys Must Be Unique As a Dictionary Cannot Have Repeated Keys.")
        return

    result = create_dict_from_lists(keys, values)

    print()
    print(f"The Keys List Is : {keys}")
    print(f"The Values List Is : {values}")
    print(f"The Generated Dictionary Is : {result}")

if __name__ == "__main__":
    main()
