# Создаем список
elements = ["яблоко", 42, True, 3.14]

# Создаем словарь, где каждый элемент - и ключ, и значение
result_dict = {}
for item in elements:
    result_dict[item] = item

print(result_dict)