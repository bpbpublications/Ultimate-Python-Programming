def func(x, y):
    x += y


L1 = [5, 6]
L2 = [7, 8]
func(L1, L2)

t1 = (5, 6)
t2 = (7, 8)
func(t1, t2)

print(L1, t1)
