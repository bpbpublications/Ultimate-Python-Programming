d = 6


def func(p=None):
    if p is None:
        p = d
    print(p, end = '  ')


func()
func(80)

d = 100
func()

d += 20
func()
