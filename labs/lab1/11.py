nums = input("Задание 11: Введите 3 числа через запятую: ")
a, b, c = nums.split(",")
a, b, c = int(a), int(b), int(c)
calc = (a + c) // b
print(f"Результат вычисления: {calc}")