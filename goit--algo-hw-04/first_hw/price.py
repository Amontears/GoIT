import re

def total_price(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        total_price_value = 0

        for line in lines:
            match = re.match(r"([A-Za-z\s]+)\.(\d+)", line.strip())
            if match:
                product, price_str = match.groups()

                total_price_value += float(price_str)
            else:
                print(f"Помилка: Некоректний формат рядка - {line.strip()}")

        average_price_value = total_price_value / len(lines)

        return total_price_value, average_price_value

    except FileNotFoundError:
        print(f"Помилка: Файл {path} не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

path = r"X:\GoIT\GoIT\goit--algo-hw-04\first_hw\price.txt"

result = total_price(path)

if result is not None:
    total_value, average_value = result
    print(f"Загальна сума бонусів: {total_value}, Середній бонус: {average_value}")
else:
    print("Отримано None від функції.")
