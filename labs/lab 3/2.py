number = int(input("Введите число от 1 до 9: "))

if 1 <= number <= 9:
    print(f"Таблица умножения для числа {number}:")
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")
else:
    print("Ошибка! Введите число от 1 до 9.")
   