def counter(func):
    count = 0

    def wrapper():
        nonlocal count
        count += 1
        print(count, end=' ')
        func()

    return wrapper


@counter
def func1():
    print('Hello', end='. ')


func1()
func1()
func1()
