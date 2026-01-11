evaluations = [
    {"name": "Agent Cole", "score": 78},
    {"name": "Dr. Weiss", "score": 92},
    {"name": "Technician Moore", "score": 61},
    {"name": "Researcher Lin", "score": 88}
]

# Определение сотрудника с наивысшей оценкой
best_employee = max(evaluations, key=lambda emp: emp["score"])

print(f"Сотрудник с наивысшей оценкой: {best_employee['name']} - {best_employee['score']} баллов")

# Дополнительно: вывод всех оценок для наглядности
print("\nВсе оценки сотрудников:")
for emp in evaluations:
    print(f"{emp['name']}: {emp['score']} баллов")