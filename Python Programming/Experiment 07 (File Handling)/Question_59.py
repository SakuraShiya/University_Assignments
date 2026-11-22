# Write a Python Program To Store Name, Population & Area Of N Cities In a File & Show Details, Cities Over 1 Million & Total Area.

from math import isfinite
from pathlib import Path

CITIES_FILE: Path = Path(__file__).with_name("Cities.txt")
MILLION: int = 1_000_000

def write_cities(cities: list[tuple[str, int, float]]) -> None:
    """ Write Each City As a Comma Separated Line In The Cities File """
    with open(CITIES_FILE, "w", encoding="utf-8") as file:
        for name, population, area in cities:
            file.write(f"{name},{population},{area}\n")

def read_cities() -> list[tuple[str, int, float]]:
    """ Read The Cities File & Convert Each Line Back Into a (Name, Population, Area) Tuple """
    cities: list[tuple[str, int, float]] = []

    with open(CITIES_FILE, "r", encoding="utf-8") as file:
        for line in file:
            name, population, area = line.strip().split(",")
            cities.append((name, int(population), float(area)))

    return cities

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Cities : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    cities: list[tuple[str, int, float]] = []

    for i in range(1, n + 1):
        print()
        name = input(f"Please Enter The Name Of City {i} : ").strip()

        if not name or "," in name:
            print("Invalid Input, City Name Cannot Be Empty Or Contain a Comma.")
            return

        try:
            population = int(input("Please Enter The Population : "))
            area = float(input("Please Enter The Area (In Sq. Km) : "))
        except ValueError:
            print("Invalid Input, Please Enter Valid Numbers For Population & Area.")
            return

        if population <= 0 or not isfinite(area) or area <= 0:
            print("Invalid Input, Please Enter Positive Values For Population & Area.")
            return

        cities.append((name, population, area))

    write_cities(cities)
    stored_cities = read_cities()

    large_cities = [name for name, population, _ in stored_cities if population > MILLION]
    total_area = sum(area for _, _, area in stored_cities)

    print()
    print(f"Details Of All The Cities (Saved To {CITIES_FILE.name}) :")
    for name, population, area in stored_cities:
        print(f"City Name : {name}, Population : {population:,}, Area : {area:.2f} Sq. Km")

    print()
    print(f"Cities With More Than 1 Million Population : {', '.join(large_cities) if large_cities else 'None'}")
    print(f"Sum Of Area Of All The Cities : {total_area:.2f} Sq. Km")

if __name__ == "__main__":
    main()
