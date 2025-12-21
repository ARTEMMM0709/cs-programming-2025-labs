# Создаем список
numbers = [5, 2, 7, 3, 9, 1, 4, 6, 8, 10]

# Находим индекс числа 3 и заменяем его на 30
for i in range(len(numbers)):
    if numbers[i] == 3:
        numbers[i] = 30

print(numbers)