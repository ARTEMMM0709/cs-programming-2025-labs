def is_palindrome(text: str) -> bool:
   
    #Проверяет, является ли строка палиндромом
    
    #Правила:
    #- Игнорируются пробелы, регистр и знаки препинания
    #- Сравниваются только буквы и цифры
    
    #Args:
        #text: строка для проверки
        
    #Returns:
        #True если строка - палиндром, иначе False
    
    # Очистка строки
    cleaned = ""
    for char in text.lower():
        if char.isalnum():  # Проверяем, является ли символ буквой или цифрой
            cleaned += char
    
    # Проверка на палиндром
    return cleaned == cleaned[::-1]


def check_palindrome():
    
    #Основная функция для проверки палиндрома

    text = input("Введите строку: ")
    
    if is_palindrome(text):
        return "Да"
    else:
        return "Нет"


# Пример использования
if __name__ == "__main__":
    # Примеры из задания
    test_cases = [
        "А роза упала на лапу Азора",
        "Borrow or rob",
        "Алфавитный порядок"
    ]
    
    for test in test_cases:
        print(f"'{test}' -> {check_palindrome(test)}")