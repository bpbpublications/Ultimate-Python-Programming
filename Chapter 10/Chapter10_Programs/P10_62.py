def func(a, b, /, x, y):
    print(a, b, x, y)

func(1, 2, 3, 5)  # correct
func(1, 2, 3, y=5)  # correct

#func(1, b=2, x=3, y=4)
#func(a=1, b=2, x=3, y=4)

#len(obj = [1,2,3,4])
