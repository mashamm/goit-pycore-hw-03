import datetime


def get_days_from_today(date):
    """
    Calculate the number of days between today and the given date.

    Args:
        date: A string in 'YYYY-MM-DD' format.

    Returns:
        int: Positive if the date is in the past, negative if in the future.
             E.g., get_days_from_today("2021-10-09") returns -157 when today
             is 2021-05-05 (Oct 9 is 157 days later).

    Raises:
        ValueError: If the date format is invalid.
    """
    try:
        input_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")  
    today = datetime.date.today()
    delta = today - input_date
    return delta.days

def main():
    print(get_days_from_today(input("Enter a date in YYYY-MM-DD format: ")))

if __name__ == '__main__':
    main()