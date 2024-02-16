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
                days_until_birthday += 7 - birthday.weekday()

            congratulation_date = today.replace(day=today.day + days_until_birthday)

            if congratulation_date.weekday() >= 5:
                congratulation_date = congratulation_date.replace(
                    day=congratulation_date.day + (7 - congratulation_date.weekday())
                )

            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")

            upcoming_birthdays.append(
                {"name": user["name"], "Дата привітання": congratulation_date_str}
            )
        else:
            pass

    return upcoming_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)
if upcoming_birthdays:
    print("Найближче привітання:", upcoming_birthdays[0])
else:
    print("Немає найближчих привітань")


#   При запуску коду виведе : Найближче привітання: {'name': 'Сергій Бабенко', 'Дата привітання': '2024.01.30'} =)
#   Дякую за увагу.
