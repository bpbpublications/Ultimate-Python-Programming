def func(a, b):
    print(a + b)


print(type(func))
print(id(func))
print(func)

func = 2
print(func)


def func(a, b):
    print(a + b)


print(func)

add = func
add(1, 2)
func(1, 3)
