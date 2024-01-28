#  HOMEWORK 3
#  Домашнє завдання 1

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



import random

def get_numbers_ticket(minimum, maximum, quantity):
    # Перевірка вхідних даних
    if not (1 <= minimum <= maximum <= 1000) or not (1 <= quantity <= maximum - minimum + 1):
        print("Некоректні параметри. Перевірте вхідні дані.")
        return []

    # Генерація унікальних чисел
    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(minimum, maximum))

    # Сортування та повернення результату
    return sorted(list(numbers_set))

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)



import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    cleaned_number = re.sub(r'\D', '', phone_number)

    # Перевіряємо, чи номер починається з '+'
    if not cleaned_number.startswith('+'):
        # Додаємо міжнародний код '+38', якщо його немає
        cleaned_number = '+38' + cleaned_number

    return cleaned_number

# Приклад використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)





users = [
    {"name": "Сергій Бабенко", "birthday": "1985.01.30"},
    {"name": "Юлія Стерненко", "birthday": "1990.01.31"},
    {"name": "Аліса Нечепорук", "birthday": "1988.02.15"},
    {"name": "Валерій Шандро", "birthday": "1995.03.20"},
    {"name": "Юрій Дідуховский", "birthday": "1987.04.25"},
    {"name": "Яна Мельник", "birthday": "1992.05.10"},
]

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday = birthday.replace(year=today.year)

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday.weekday() >= 5:
                days_until_birthday += (7 - birthday.weekday())

            congratulation_date = today.replace(day=today.day + days_until_birthday)

            if congratulation_date.weekday() >= 5:
                congratulation_date = congratulation_date.replace(day=congratulation_date.day + (7 - congratulation_date.weekday()))

            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")

            upcoming_birthdays.append({"name": user["name"], "Дата привітання": congratulation_date_str})
        else:
            pass

    return upcoming_birthdays



upcoming_birthdays = get_upcoming_birthdays(users)
if upcoming_birthdays:
    print("Найближче привітання:", upcoming_birthdays[0])
else:
    print("Немає найближчих привітань")
