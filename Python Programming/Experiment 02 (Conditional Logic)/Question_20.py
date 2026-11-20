# Write a Python Program To Take Any Date As Input & Display Next Date Of The Calendar.

def check_leap_year(year: int) -> bool:
    """ Check Whether a Given Year Is a Leap Year """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_next_date(day: int, month: int, year: int, max_days: int) -> tuple[int, int, int]:
    """ Compute & Return The Next Calendar Date Given a Valid Date & Month Length """
    if day < max_days:
        return day + 1, month, year
    if month == 12:
        return 1, 1, year + 1
    return 1, month + 1, year

def main() -> None:
    try:
        day = int(input("Please Enter a Day : "))
        month = int(input("Please Enter a Month : "))
        year = int(input("Please Enter a Year : "))
    except ValueError:
        print("Invalid Input, Please Enter Valid Numbers For Day, Month & Year.")
        return

    if year <= 0:
        print("Invalid Input, Please Enter a Positive Calendar Year.")
        return

    if not (1 <= month <= 12):
        print("Invalid Month, Please Enter a Valid Month Between 1 & 12.")
        return

    is_leap = check_leap_year(year)
    month_days = (31, 29 if is_leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    max_days = month_days[month - 1]

    if not (1 <= day <= max_days):
        print(f"Invalid Day, Please Enter a Day Between 1 & {max_days}.")
        return

    next_day, next_month, next_year = get_next_date(day, month, year, max_days)

    print(f"You Entered The Date As : {day}/{month}/{year}")
    print(f"The Next Date Is : {next_day}/{next_month}/{next_year}")

if __name__ == "__main__":
    main()
