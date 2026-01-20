# Создаем список слов
fruits = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]

# Создаем пустой словарь
result = {}

# Заполняем словарь
for fruit in fruits:
    first_letter = fruit[0]  # Получаем первую букву
    
    # Если такой буквы еще нет в словаре, создаем пустой список
    if first_letter not in result:
        result[first_letter] = []
    
    # Добавляем слово в список для этой буквы
    result[first_letter].append(fruit)

print(result)