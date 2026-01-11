scp_objects = [
    {"scp": "SCP-096", "class": "Euclid"},
    {"scp": "SCP-173", "class": "Euclid"},
    {"scp": "SCP-055", "class": "Keter"},
    {"scp": "SCP-999", "class": "Safe"},
    {"scp": "SCP-3001", "class": "Keter"}
]

# Фильтрация SCP-объектов, требующих усиленных мер (класс не Safe)
enhanced_containment_scps = list(filter(
    lambda scp: scp["class"] != "Safe",
    scp_objects
))

print("SCP-объекты, требующие усиленных мер содержания:")
for scp in enhanced_containment_scps:
    print(f"{scp['scp']} - Класс: {scp['class']}")