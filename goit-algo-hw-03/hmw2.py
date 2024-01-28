import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum <= maximum <= 1000) or not (1 <= quantity <= maximum - minimum + 1):
        print("Некоректні параметри. Перевірте вхідні дані.")
        return []
    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(minimum, maximum))
    return sorted(list(numbers_set))
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


#   При запуску коду виведе : Ваші лотерейні числа: [7, 8, 23, 26, 32, 40] 