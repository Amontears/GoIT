def get_cats_info(path):
    try:
        cats_info = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # Розділити рядок на ідентифікатор, ім'я та вік
                cat_id, name, age = line.strip().split(',')
                
                # Створити словник з інформацією про кота та додати його до списку
                cat_info = {"id": cat_id, "name": name, "age": age}
                cats_info.append(cat_info)

        return cats_info

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []

# Шлях до файлу
file_path = r"X:\GoIT\GoIT\goit--algo-hw-04\first_hw\cats_file.txt"

# Використання функції та виведення результату
cats_info = get_cats_info(file_path)
print(cats_info)
