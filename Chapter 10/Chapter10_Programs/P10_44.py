def func(a, L=None):
    if L is None:
        L = []
    L.append(a)
    print(L)


func(10, [1, 2, 3])
func(8, [5, 6])
func(9)
func('Hello')
func(100)
