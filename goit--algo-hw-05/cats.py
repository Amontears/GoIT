def get_cats_info(path):
    try:
        cats_info = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                
                cat_info = {"id": cat_id, "name": name.capitalize(), "age": age}
                cats_info.append(cat_info)

        return cats_info

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []

file_path = r"X:\GoIT\GoIT\goit--algo-hw-04\second_hw\cats.txt"

cats_info = get_cats_info(file_path)
for cat_info in cats_info:
    print(cat_info)



#Резудтат буде : 
#{'id': '60b90c1c13067a15887e1ae1', 'name': 'Tayler', 'age': '3'}
#{'id': '60b90c2413067a15887e1ae2', 'name': 'Vendi', 'age': '1'}
#{'id': '60b90c2e13067a15887e1ae3', 'name': 'Bars', 'age': '2'}
#{'id': '60b90c3b13067a15887e1ae4', 'name': 'Nika', 'age': '12'}
#{'id': '60b90c4613067a15887e1ae5', 'name': 'Lala', 'age': '5'}




