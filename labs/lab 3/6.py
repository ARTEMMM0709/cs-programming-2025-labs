temp_num_array = [0,1]
print('введите число')
user_num = int(input())
temp_sum = 0
while(user_num>temp_sum):
    temp_sum = temp_num_array[0]+temp_num_array[1]
    print(temp_sum)
    temp_num_array[0] = temp_num_array[1]
    temp_num_array[1] = temp_sum