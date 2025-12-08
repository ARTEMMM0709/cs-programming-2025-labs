special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?~" #Строка содержащая все спец.символы
#Флаги отвечающие за надёжность пароля
has_spec = False
has_up = False
has_low = False
has_digit = False
result = "Пароль ненадёжный: отсутствуют " #Создаём шаблон строки вывода

password = input('Введите пароль:')
for char in password: #Перебираем пароль посимвольно
    if char in special_chars: #Проверяем на наличие спец.символов
        has_spec = True
    if char.islower(): #Проверяем на наличие строчных букв
        has_low = True
    if char.isupper(): #Проверяем на наличие заглавных букв
        has_up = True
    if char.isdigit(): #Проверяем на наличие чисел
        has_digit = True  
if has_digit and has_up and has_low and has_spec: #Если все условия соблюдены, то пароль надёжен
        print('Пароль надёжный')
else:
    #Ниже добавляем к строке части в зависимости от того, что в нём отсутвует
    if has_spec == False:
        result += 'специальные символы, '
    if has_up == False:
        result += 'заглавные буквы, '
    if has_low == False:
        result += 'строчные буквы, '
    if has_digit == False:
        result += 'числа, '
    print(result[0:-2]) #Удаляем из строки 2 последних символа ()лишний пробел и запятую
