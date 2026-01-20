# Создание списка словарей с SCP-объектами и их классами
# Каждый словарь содержит номер SCP и класс опасности
scp_objects = [
    {"scp": "SCP-096", "class": "Euclid"},   # Объект класса Euclid
    {"scp": "SCP-173", "class": "Euclid"},   # Объект класса Euclid
    {"scp": "SCP-055", "class": "Keter"},    # Объект класса Keter
    {"scp": "SCP-999", "class": "Safe"},     # Объект класса Safe
    {"scp": "SCP-3001", "class": "Keter"}    # Объект класса Keter
]

# Фильтрация объектов: оставляем только те, которые НЕ имеют класс "Safe"
# Lambda-функция проверяет условие: класс объекта не равен "Safe"
enhanced_security_scps = list(filter(lambda obj: obj["class"] != "Safe", scp_objects))

# Вывод поясняющего заголовка
print("Список SCP-объектов, которые требуют усиленных мер содержания: ")

# Вывод отфильтрованного списка
# В результате останутся все объекты, кроме SCP-999 (класс Safe)
print(enhanced_security_scps)