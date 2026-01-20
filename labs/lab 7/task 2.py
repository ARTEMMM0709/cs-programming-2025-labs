# Создание списка словарей с данными сотрудников
# Каждый словарь содержит имя, стоимость смены и количество смен
staff_shifts = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
]

# Использование map() с lambda-функцией для вычисления общей стоимости для каждого сотрудника
# Lambda умножает shift_cost на shifts для каждого словаря person
costs = list(map(lambda person: person["shift_cost"] * person["shifts"], staff_shifts))

# Вывод списка общих стоимостей
print("Список общей стоимости:", costs)

# Поиск максимального значения в списке costs
max_cost = max(costs)

# Вывод максимальной стоимости
print("Максимальная стоимость:", max_cost)