# Создаем список студентов с оценками
students = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]

# Создаем словарь с средними оценками
averages = {}
for name, grades in students:
    avg = sum(grades) / len(grades)
    averages[name] = avg

# Находим студента с максимальной средней оценкой
best_student = max(averages, key=averages.get)
best_avg = averages[best_student]

print(f"{best_student} имеет наивысший средний балл: {best_avg}")