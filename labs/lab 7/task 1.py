objects = [
    ("Containment Cell A", 4),
    ("Archive Vault", 1),
    ("Bio Lab Sector", 3),
    ("Observation Wing", 2)
]

# Сортировка объектов по уровню угрозы
sorted_objects = sorted(objects, key=lambda x: x[1])
print("Объекты, отсортированные по уровню угрозы:")
for obj in sorted_objects:
    print(f"{obj[0]} - Уровень угрозы: {obj[1]}")