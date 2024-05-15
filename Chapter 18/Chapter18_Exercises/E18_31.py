class Accepts:
    def __init__(self, *types):
        self.types = types

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            if kwargs:
                print('Keyword arguments not allowed')

            for argument, type in zip(args, self.types):
                if not isinstance(argument, type):
                    raise ValueError('Invalid argument type')
            return fn(*args)
        return wrapper

@Accepts(int, float, int, int)
def func1(x, y, z):
    print(x, y, z)

@Accepts(int, str, str, list)
def func2(p, q, r, s):
    print(p, q, r, s)

@Accepts(int)
def func3(a, b, c):
    print(a, b, c)

@Accepts(str, int)
def func4(a, b, c, d, e, f):
    print(a, b, c, d, e, f)

func1(1, 1.2, 3)
func2(2, 'ab', 'cd', [3, 4, 5])
func3(1, 'sds', 45)
func4('xy', 2, 4, 5, 6, 7)
