zones = [
    {"zone": "Sector-12", "active_from": 8, "active_to": 18},
    {"zone": "Deep Storage", "active_from": 0, "active_to": 24},
    {"zone": "Research Wing", "active_from": 9, "active_to": 17}
]

# Фильтрация зон, работающих полностью в дневной период (8-18)
daytime_zones = list(filter(
    lambda zone: zone["active_from"] >= 8 and zone["active_to"] <= 18,
    zones
))

print("Зоны, работающие полностью в дневной период (8-18):")
for zone in daytime_zones:
    print(f"{zone['zone']}: с {zone['active_from']} до {zone['active_to']}")