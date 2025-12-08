try:
    #Запрашиваем 3 числа и создаём список на основе введённых чисел
    numbers = input('Введите три числа:').split()
    num1 = int(numbers[0])
    num2 = int(numbers[1])
    num3 = int(numbers[2])
    #Проверяем что пользователь ввёл именно 3 числа
    if len(numbers) != 3:
        print('Вы ввели не три числа')
    else:
        #Ищем наибольшее из первых двух чисел, чтобы сравнить его с третьим
        if num1 < num2:
            if num1 < num3:
                smallest = num1
            else:
                smallest = num3
        else:
            if num2 < num3:
                smallest = num2
            else:
                smallest = num3
        print('Наименьшее число:',smallest)
except ValueError:
    print('Число введенно неверно')

