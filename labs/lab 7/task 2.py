staff_shifts = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
]

# Создание списка общей стоимости работы каждого сотрудника
total_costs = list(map(lambda emp: emp["shift_cost"] * emp["shifts"], staff_shifts))
print("Общая стоимость работы каждого сотрудника:", total_costs)

# Нахождение максимальной стоимости
max_cost = max(total_costs)
print(f"Максимальная стоимость работы: {max_cost}")

# Если нужно также узнать имя сотрудника с максимальной стоимостью:
max_employee = max(staff_shifts, key=lambda emp: emp["shift_cost"] * emp["shifts"])
print(f"Сотрудник с максимальной стоимостью: {max_employee['name']} - {max_employee['shift_cost'] * max_employee['shifts']}")