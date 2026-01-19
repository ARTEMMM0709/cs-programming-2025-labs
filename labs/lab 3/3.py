a = input('').split()
cnt_colors = 1
x = int(a[0])
y = int(a[1])
r = int(a[2])
if y <= r or x <= r:
    cnt_colors += 1
if x < r:
    cnt_colors += 1
if x ** 2 + y  **2 < r ** 2:
    cnt_colors += 1
if y < r:
    cnt_colors += 1
print(cnt_colors)