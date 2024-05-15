class MyDecoratorWithArgs:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2
        print(f'Decorator arguments {a1}, {a2}')

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            print('Executed Before function call')
            result = fn(*args, **kwargs)
            print('Executed After function call\n')
            return result

        return wrapper


@MyDecoratorWithArgs('Hello', 10)
def func1():
    print('func1 executing')


@MyDecoratorWithArgs(10, 12)
def func2(a, b):
    print('func2 executing')


def func3():
    print('func3 executing')


func3 = MyDecoratorWithArgs(3, 5)(func3)

func1()
func2(1, 2)
func3()
