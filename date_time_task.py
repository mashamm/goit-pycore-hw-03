import datetime
def get_days_from_today(date):
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