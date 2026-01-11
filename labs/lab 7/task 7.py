incidents = [
    {"id": 101, "staff": 4},
    {"id": 102, "staff": 12},
    {"id": 103, "staff": 7},
    {"id": 104, "staff": 20}
]

# 1. Сортировка инцидентов по количеству персонала (по убыванию)
sorted_incidents = sorted(incidents, key=lambda x: x["staff"], reverse=True)

print("Все инциденты, отсортированные по количеству персонала (по убыванию):")
for incident in sorted_incidents:
    print(f"Инцидент {incident['id']}: {incident['staff']} сотрудников")

print("\n" + "="*40 + "\n")

# 2. Оставление только трех наиболее ресурсоемких инцидентов
top_3_incidents = sorted_incidents[:3]

print("Три наиболее ресурсоемких инцидента:")
for incident in top_3_incidents:
    print(f"Инцидент {incident['id']}: {incident['staff']} сотрудников")