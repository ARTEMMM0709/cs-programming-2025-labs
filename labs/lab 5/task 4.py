# Создаем кортеж
my_tuple = (5, 2, 8, 1, 3)

# Пробуем отсортировать
try:
    sorted_tuple = tuple(sorted(my_tuple))
    print(sorted_tuple)
except TypeError:
    # Если возникает ошибка (не все элементы числа), оставляем как есть
    print(my_tuple)