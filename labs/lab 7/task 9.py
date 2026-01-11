shifts = [6, 12, 8, 24, 10, 4]

# Фильтрация смен по длительности (от 8 до 12 часов включительно)
filtered_shifts = list(filter(
    lambda duration: 8 <= duration <= 12,
    shifts
))

print("Все смены:", shifts)
print("Смены от 8 до 12 часов:", filtered_shifts)
print("\nПодробно:")
for i, duration in enumerate(filtered_shifts, 1):
    print(f"Смена {i}: {duration} часов")