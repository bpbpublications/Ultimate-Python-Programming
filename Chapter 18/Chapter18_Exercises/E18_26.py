from functools import update_wrapper

class CountNumberOfCalls:
    def __init__(self, fn):
        update_wrapper(self, fn)
        self.func = fn
        self.number_of_calls = 0

    def __call__(self, *args, **kwargs):
        self.number_of_calls += 1
        return self.func(*args, **kwargs)

@CountNumberOfCalls
def func1():
    print('Hello', end='. ')

func1()
func1()
func1()
print(func1.number_of_calls)
