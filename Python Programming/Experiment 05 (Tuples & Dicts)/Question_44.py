# Write a Python Program To Create a Dictionary Of N Persons Where Key Is Name & Value Is City.

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Persons : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    persons: dict[str, str] = {}

    for i in range(1, n + 1):
        name = input(f"Please Enter The Name Of Person {i} : ").strip().title()

        if not name:
            print("Invalid Input, Name Cannot Be Empty.")
            return

        if name in persons:
            print(f"Invalid Input, {name} Has Already Been Entered.")
            return

        city = input(f"Please Enter The City Of Person {i} : ").strip().title()

        if not city:
            print("Invalid Input, City Cannot Be Empty.")
            return

        persons[name] = city

    city_count: dict[str, int] = {}

    for city in persons.values():
        city_count[city] = city_count.get(city, 0) + 1

    print()
    print(f"Names Of All Persons : {', '.join(persons)}")
    print(f"Cities Of All Persons : {', '.join(persons.values())}")

    print()
    print("Name & City Of All Persons :")
    for name, city in persons.items():
        print(f"{name} : {city}")

    print()
    print("Number Of Persons In Each City :")
    for city, count in city_count.items():
        print(f"{city} : {count}")

if __name__ == "__main__":
    main()
