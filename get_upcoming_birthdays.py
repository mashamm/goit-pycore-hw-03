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

    # Set of (month, day) pairs for today through today+7 days (8 dates total)
    upcoming_month_days = {
        ((today + datetime.timedelta(days=i)).month, (today + datetime.timedelta(days=i)).day)
        for i in range(8)
    }
    upcoming = []

    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # Skip if birthday (month, day) is not in the next 7 days
        if (birthday.month, birthday.day) not in upcoming_month_days:
            continue

        # Find actual date in range — handles year boundary (e.g. Dec 30 → Jan 2)
        for i in range(8):
            d = today + datetime.timedelta(days=i)
            if (d.month, d.day) == (birthday.month, birthday.day):
                congratulation_date = d
                break

        # Move weekend to next Monday: Saturday (+2 days), Sunday (+1 day)
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
        {"name": "Jane Smith", "birthday": "1990.02.16"},
    ]
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)


if __name__ == "__main__":
    main()
