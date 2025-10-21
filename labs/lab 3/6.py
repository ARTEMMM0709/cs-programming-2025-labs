n = int(input("Введите число: "))
a, b = 0, 1
while a <= n:
    print(a)
    a, b = b, a + b
