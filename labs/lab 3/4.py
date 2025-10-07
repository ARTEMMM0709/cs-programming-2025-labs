print('введите число')
number = int(input())
final_integer = 1
for i in range(number):
    final_integer *= (i+1)
print(final_integer)