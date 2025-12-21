import random

# Определяем возможные варианты
options = ["камень", "ножницы", "бумага", "ящерица", "спок"]

# Правила победы
rules = {
    "ножницы": ["бумага", "ящерица"],
    "бумага": ["камень", "спок"],
    "камень": ["ящерица", "ножницы"],
    "ящерица": ["спок", "бумага"],
    "спок": ["ножницы", "камень"]
}

# Получаем выбор пользователя
user_choice = input("Выберите: камень, ножницы, бумага, ящерица, спок: ").lower()

if user_choice not in options:
    print("Неверный выбор!")
else:
    # Компьютер выбирает случайно
    computer_choice = random.choice(options)
    print(f"Компьютер выбрал: {computer_choice}")
    
    # Определяем победителя
    if user_choice == computer_choice:
        print("Ничья!")
    elif computer_choice in rules[user_choice]:
        print("Вы победили!")
    else:
        print("Компьютер победил!")