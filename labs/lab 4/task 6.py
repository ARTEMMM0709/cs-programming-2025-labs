try:
    year = int(input('Введите год:')) #Запрашиваем год
    #Год високосный, если его последнее цисло кратно 4 и год не кратен 100
    #или год кратен 400
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: 
        result = 'високосный'
    else:
        result = 'не високосный'
    print(year,'-',result,'год')
except ValueError:
    print('Число введенно неверно')