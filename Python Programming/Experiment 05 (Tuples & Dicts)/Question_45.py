# Write a Python Program To Store Details Of N Movies In a Dictionary By Taking Input From The User.

from datetime import date
from math import isfinite

CUTOFF_YEAR: int = 2015
FIRST_FILM_YEAR: int = 1888
CURRENT_YEAR: int = date.today().year

def analyse_movies(movies: dict[str, tuple[int, str, float, float]], director: str) -> dict[str, list[str]]:
    """ Find The Movies Released Before 2015, Movies That Made a Profit & Movies Directed By The Given Director """
    return {
        f"Movies Released Before {CUTOFF_YEAR} Are": [name for name, (year, _, _, _) in movies.items() if year < CUTOFF_YEAR],
        "Movies That Made a Profit Are": [name for name, (_, _, cost, collection) in movies.items() if collection > cost],
        f"Movies Directed By {director} Are": [name for name, (_, by, _, _) in movies.items() if by.lower() == director.lower()],
    }

def format_names(names: list[str]) -> str:
    """ Return The Names As Comma Separated Text Or None """
    return ", ".join(names) if names else "None"

def main() -> None:
    try:
        n = int(input("Please Enter The Number Of Movies : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number.")
        return

    if n < 1:
        print("Invalid Input, Please Enter a Positive Integer.")
        return

    movies: dict[str, tuple[int, str, float, float]] = {}

    for i in range(1, n + 1):
        print()

        try:
            name = input(f"Please Enter The Name Of Movie {i} : ").strip()
            year = int(input("Please Enter The Year Of Release : "))
            director = input("Please Enter The Director Name : ").strip()
            cost = float(input("Please Enter The Production Cost (In Crore) : "))
            collection = float(input("Please Enter The Collection Made (In Crore) : "))
        except ValueError:
            print("Invalid Input, Please Enter Valid Numbers For Year, Cost & Collection.")
            return

        if not name or not director:
            print("Invalid Input, Movie Name & Director Name Cannot Be Empty.")
            return

        if name.lower() in (movie.lower() for movie in movies):
            print(f"Invalid Input, Movie '{name}' Has Already Been Entered.")
            return

        if not (FIRST_FILM_YEAR <= year <= CURRENT_YEAR):
            print(f"Invalid Input, Year Of Release Must Be Between {FIRST_FILM_YEAR} & {CURRENT_YEAR}.")
            return

        if not (isfinite(cost) and isfinite(collection)) or cost <= 0 or collection < 0:
            print("Invalid Input, Please Enter Finite Positive Values For Cost & Collection.")
            return

        movies[name] = (year, director, cost, collection)

    print()
    print("All Movie Details Are As Follows :")
    for name, (year, director, cost, collection) in movies.items():
        print(f"Movie Name : {name}")
        print(f"Year Of Release : {year}")
        print(f"Director's Name : {director}")
        print(f"Production Cost : {cost:.2f} Crore")
        print(f"Collection Made : {collection:.2f} Crore")
        print()

    search_director = input("Please Enter The Director Name To Find Movies Directed By Him/Her : ").strip()

    if not search_director:
        print("Invalid Input, Director Name Cannot Be Empty.")
        return

    results = analyse_movies(movies, search_director)

    print()
    for description, names in results.items():
        print(f"{description} : {format_names(names)}")

if __name__ == "__main__":
    main()
