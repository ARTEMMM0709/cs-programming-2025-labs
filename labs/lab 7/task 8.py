protocols = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
]

# Создание нового списка строк по заданному формату
formatted_protocols = list(map(
    lambda protocol: f"Protocol {protocol[0]} - Criticality {protocol[1]}",
    protocols
))

print("Форматированные протоколы:")
for protocol in formatted_protocols:
    print(protocol)