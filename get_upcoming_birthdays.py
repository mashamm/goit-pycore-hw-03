import datetime


def get_upcoming_birthdays(users):
    """
    Get list of colleagues to congratulate in the next 7 days (including today).

    If birthday falls on weekend, congratulation date is moved to next Monday.

    Args:
        users: List of dicts with 'name' (str) and 'birthday' (str, 'YYYY.MM.DD').

    Returns:
        list: List of dicts with 'name' and 'congratulation_date' (str, 'YYYY.MM.DD').
    """
    today = datetime.date.today()
    upcoming_month_days = {
        ((today + datetime.timedelta(days=i)).month, (today + datetime.timedelta(days=i)).day)
        for i in range(8)
    }
    upcoming = []

    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        if (birthday.month, birthday.day) not in upcoming_month_days:
            continue

        for i in range(8):
            d = today + datetime.timedelta(days=i)
            if (d.month, d.day) == (birthday.month, birthday.day):
                congratulation_date = d
                break
        weekday = congratulation_date.weekday()

        if weekday == 5:
            congratulation_date += datetime.timedelta(days=2)
        elif weekday == 6:
            congratulation_date += datetime.timedelta(days=1)

        upcoming.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
        })

    return upcoming


def main():
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)


if __name__ == "__main__":
    main()
