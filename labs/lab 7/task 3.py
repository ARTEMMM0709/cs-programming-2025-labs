personnel = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]

# Определение категории допуска на основе уровня
def get_clearance_category(level):
    if level == 1:
        return "Restricted"
    elif 2 <= level <= 3:
        return "Confidential"
    else:  # level >= 4
        return "Top Secret"

# Создание нового списка с категориями допуска
personnel_with_categories = list(
    map(lambda emp: {
        "name": emp["name"],
        "clearance": emp["clearance"],
        "category": get_clearance_category(emp["clearance"])
    }, personnel)
)

print("Персонал с категориями допуска:")
for emp in personnel_with_categories:
    print(f"{emp['name']} - Уровень: {emp['clearance']}, Категория: {emp['category']}")