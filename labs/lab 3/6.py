limit = int(input("Введите число для вывода чисел Фибоначчи: "))

a, b = 0, 1
print(f"Числа Фибоначчи до {limit}:")
while a <= limit:
    print(a, end=" ")
    a, b = b, a + b
print()