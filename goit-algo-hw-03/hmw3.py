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
import re
def normalize_phone(phone_number):
    cleaned_number = re.sub(r'\D', '', phone_number)
    if not cleaned_number.startswith('+'):
        cleaned_number = '+38' + cleaned_number
    return cleaned_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


#   При запуску коду виведе : Нормалізовані номери телефонів для SMS-розсилки: ['+380671234567', '+380952345678', '+38380441234567', '+38380501234567', '+38380501233234', '+380503451234', '+380508889900', '+38380501112222', '+38380501112211']