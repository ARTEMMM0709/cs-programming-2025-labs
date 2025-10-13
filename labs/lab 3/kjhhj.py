b = int(input('введите номер от отного до 256:'))
b = bin(b)[2:]
while len(b) !=8:
     b = '0' + b
q = 0
otv = []
all =[]
print('x y z f')
for i in range(0,1):
    for o in range(0,1):
        for p in range(0,1):
            if b[q] == '1':
                for e in i,o,p:
                    if e == 0:
                        otv.append('not ')
                    else:
                        otv.append('')
            if b[q] == '0':
                print(i,o,p,b[q])
            else:
                print(i,o,p,b[q],f'{otv[0]} x and {otv[1]} y and {otv[0]} z')
                all.append(f'{otv[0]} x and {otv[1]} y and {otv[2]} z')
            q +=1
            otv = []
print(' or'.join(all))