# Write a Python Program To Convert Given Seconds Into Hours, Minutes & Remaining Seconds.

SECONDS_PER_HOUR: int = 3600
SECONDS_PER_MINUTE: int = 60

def format_unit(value: int, unit: str) -> str:
    """ Return The Value With Its Unit In Singular Or Plural Form """
    return f"{value} {unit}" if value == 1 else f"{value} {unit}s"

def main() -> None:
    try:
        seconds = int(input("Please Enter The Number Of Seconds : "))
    except ValueError:
        print("Invalid Input, Please Enter a Valid Number For Seconds.")
        return

    if seconds < 0:
        print("Invalid Input, Please Enter a Non Negative Value For Seconds.")
        return

    hours, remaining_seconds = divmod(seconds, SECONDS_PER_HOUR)
    minutes, remaining_seconds = divmod(remaining_seconds, SECONDS_PER_MINUTE)

    print(f"The Conversion Of {format_unit(seconds, 'Second')} Is : "
          f"{format_unit(hours, 'Hour')} {format_unit(minutes, 'Minute')} {format_unit(remaining_seconds, 'Second')}")

if __name__ == "__main__":
    main()
