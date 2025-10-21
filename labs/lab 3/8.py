while True:
    nums = input("Введите два числа через пробел: ").split()
    if len(nums) != 2:
        print("Введите ровно два числа!")
        continue
    try:
        a, b = float(nums[0]), float(nums[1])
        print("Сумма равна:", a + b)
    except ValueError:
        print("Ошибка ввода! Введите числа.")
