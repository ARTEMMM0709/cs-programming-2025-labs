print("Программа для сложения двух чисел ")

while True:
    try:
        numbers = input("Введите два числа через пробел: ").split()
        
        if len(numbers) != 2:
            print("Ошибка! Введите ровно два числа через пробел.")
            continue
        
        num1 = float(numbers[0])
        num2 = float(numbers[1])
        total = num1 + num2
        
        print(f"Сумма равна: {total}")
        print()
        
    except ValueError:
        print("Ошибка! Введите корректные числа.")
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")
        break