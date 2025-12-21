# Создаем словарь переводов
translations = {
    "apple": "яблоко",
    "banana": "банан",
    "cat": "кот",
    "dog": "собака"
}

# Получаем русское слово от пользователя
russian_word = input("Введите русское слово: ")

# Ищем английское соответствие
english_word = None
for eng, rus in translations.items():
    if rus == russian_word:
        english_word = eng
        break

if english_word:
    print(f"Английский перевод: {english_word}")
else:
    print("Перевод не найден")