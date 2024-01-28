from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
        today_date = datetime.today()
        date_difference = today_date - input_date
        return date_difference.days
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'")
        return None

today = datetime.today().strftime('%Y-%m-%d')  
days_difference = get_days_from_today("2021-10-09")

if days_difference is not None:
    print(f"Сьогодні {today}, а від '2021-10-09' пройшло {days_difference} днів.")