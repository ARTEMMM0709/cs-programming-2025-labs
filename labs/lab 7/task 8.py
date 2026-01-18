# Создание списка кортежей с протоколами безопасности
# Каждый кортеж содержит название протокола и уровень критичности
protocols = [
    ("Lockdown", 5),        # Протокол "Lockdown" с критичностью 5
    ("Evacuation", 4),      # Протокол "Evacuation" с критичностью 4
    ("Data Wipe", 3),       # Протокол "Data Wipe" с критичностью 3
    ("Routine Scan", 1)     # Протокол "Routine Scan" с критичностью 1
]

# Преобразование каждого кортежа в отформатированную строку:
# map() применяет lambda-функцию к каждому кортежу p в списке protocols
# f-строка создает текст вида "Protocol [название] - Criticality [уровень]"
formatted_protocols = list(map(lambda p: f"Protocol {p[0]} - Criticality {p[1]}", protocols))

# Вывод поясняющего заголовка
print("Протоколы безопасности и уровни их критичности: ")

# Вывод отформатированного списка строк
# Результат: список строк вида "Protocol Lockdown - Criticality 5" и т.д.
print(formatted_protocols)