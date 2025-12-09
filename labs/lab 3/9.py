while True:
    otv = []
    a = input(' введите 5 натуральных чисел:').split()
    print(a)
    if len(a)== 5:
        for i in range(len(a)):
            if not(a[i].replace('-','').isdigit()):
                print('ошибка введено не то число ')
                break
        else:
            a = sorted(list(map(int,a)))
            if a[0] > 0:
                for x in range(4):
                    for y in range(x,5):
                        if x < y and f'({a[x]},{a[y]})' not in otv and a[x] != a[y]:
                            otv.append(f'({a[x]},{a[y]})')
            else:
                print('введено не натуральное число')
            print(otv)
    else:
        print('введите 5 чисел')


            

