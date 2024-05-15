D1 = {1: 'a', 2: 'b'}
D2 = {1: 'a', 2: 'b'}


def func1(d):
    d = {}


def func2(d):
    d.clear()


func1(D1)
func2(D2)

print(D1, D2)
