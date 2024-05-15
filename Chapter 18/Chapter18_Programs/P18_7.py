def calls_counter(fn):
    def wrapper():
        wrapper.number_of_calls += 1
        fn()

    wrapper.number_of_calls = 0
    return wrapper


@calls_counter
def func1():
    x = 999 ** 99999


@calls_counter
def func2():
    L = [x for x in range(9999999)]


func1()
func2()
func1()
func2()
func1()

print(func1.number_of_calls)
print(func2.number_of_calls)
