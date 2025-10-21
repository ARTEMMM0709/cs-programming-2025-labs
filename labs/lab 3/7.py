s = input("Введите строку: ")
new_s = ""
for i in range(len(s)):
    new_s += s[i] + str(i + 1)
print(new_s)
