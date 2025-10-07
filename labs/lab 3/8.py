while(1):
    print('Введите два числа через пробел: ')
    user_input = input()
    temp_array = user_input.split(' ')
    sum = int(temp_array[0]) + int(temp_array[1])
    print(f'Сумма равна: {sum}')