# Создаем словарь товаров
products = {
    "яблоки": 100,
    "бананы": 80,
    "молоко": 120,
    "хлеб": 60,
    "сыр": 200
}

# Находим товары с минимальной и максимальной ценой
min_product = min(products, key=products.get)
max_product = max(products, key=products.get)

print(f"Самый дешевый: {min_product} - {products[min_product]} руб.")
print(f"Самый дорогой: {max_product} - {products[max_product]} руб.")