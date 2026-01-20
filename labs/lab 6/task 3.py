def is_prime(n: int) -> bool:

    #Проверяет, является ли число простым
    
    #Args:
        #n: число для проверки
        
    #Returns:
        #True если число простое, иначе False
   
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Проверяем делители до квадратного корня из n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_primes_in_range(start: int, end: int):
  
    #Находит все простые числа в заданном диапазоне
    
    #Args:
        #start: начало диапазона (включительно)
        #end: конец диапазона (включительно)
        
    #Returns:
        #Список простых чисел или сообщение об ошибке
  
    # Проверка корректности данных
    if start > end:
        return "Error!"
    
    # Поиск простых чисел
    primes = []
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            primes.append(num)
    
    # Если простых чисел не найдено
    if not primes:
        return "Error!"
    
    return primes


# Пример использования
if __name__ == "__main__":
    # Примеры из задания
    print(f"Диапазон 1-10: {find_primes_in_range(1, 10)}")
    print(f"Диапазон 15-120: {find_primes_in_range(15, 120)}")
    print(f"Диапазон 0-1: {find_primes_in_range(0, 1)}")