def func(**kwargs):
    for x, y in kwargs.items():
        print(x, y)


func(a=1, b=2, c=3)
func(a=1, b=2, c=3, d=4, e=5, f=6)

mydict = {'a': 1, 'b': 2, 'c': 3}
func(**mydict)
