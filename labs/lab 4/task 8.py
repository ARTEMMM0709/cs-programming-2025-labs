try:
    price = int(input('Введите сумму покупки:')) #Запрашиваем сумму
    if price < 1000: #При цене меньше 1000 скидка = 0
        discount = 0
    elif price >= 1000 and price < 5000: #При цене меньше 1000 скидка = 5
        discount = 5
    elif price >= 5000 and price <= 10000: #При цене меньше 1000 скидка = 10
        discount = 10
    else:
        #При цене не соответсвующей ни одному условию (больше 10000) скидка = 15 процентам
        discount = 15
    print('Ваша скидка:',str(discount)+'%') #Переводим скидку в строку, чтобы совместить с % без пробела
    print('К оплате:',price-price/100*discount)
except ValueError:
    print('Число введенно неверно')

