L = [1, 2, 3, 4]
flag = False
i = int(input('Enter an integer  :'))
try:
    x = L[i] + 1000
    flag = True
except IndexError as e:
    print(e)
if flag:
    print(x)

L = [1, 2, 3, 4]
i = int(input('Enter an integer  :'))
try:
    x = L[i] + 1000
except IndexError as e:
    print(e)
else:
    print(x)
