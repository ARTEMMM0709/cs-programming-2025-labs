print('введите текст')
user_input = input()
temp_str = ''
for i in range(len(user_input)):
    temp_str += user_input[i] +f'{i+1}'
print(temp_str)