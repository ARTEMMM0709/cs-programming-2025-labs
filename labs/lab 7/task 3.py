# Создание списка сотрудников с их именами и уровнем допуска
personnel = [
    {"name": "Dr. Klein", "clearance": 2},       # Уровень допуска 2
    {"name": "Agent Brooks", "clearance": 4},    # Уровень допуска 4
    {"name": "Technician Reed", "clearance": 1}  # Уровень допуска 1
]

# Применение map() с lambda-функцией для добавления категории допуска
# Lambda принимает каждый словарь x, добавляет поле "category" в зависимости от clearance
result = list(map(lambda x: {
    "name": x["name"],        # Сохраняем исходное имя
    "clearance": x["clearance"],  # Сохраняем исходный уровень допуска
    "category": (              # Определяем категорию на основе уровня допуска
        "Restricted" if x["clearance"] == 1           # Если уровень 1 -> Restricted
        else "Confidential" if 2 <= x["clearance"] <= 3  # Если уровень 2-3 -> Confidential
        else "Top Secret"                                # Иначе -> Top Secret
    )
}, personnel))  # Применяем к каждому элементу списка personnel

# Вывод заголовка для удобочитаемости
print("Список сотрудников с категорией допуска: ")

# Вывод результирующего списка словарей
print(result)