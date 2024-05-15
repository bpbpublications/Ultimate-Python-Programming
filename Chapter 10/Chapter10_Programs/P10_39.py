d = 6

def func(p=d):
    print(p, end='  ')

func()   # default argument used for parameter p
func(80)  # 80 used as argument for parameter p

d = 100
func()  # default argument used for parameter p

d += 20
func()  # default argument used for parameter p




