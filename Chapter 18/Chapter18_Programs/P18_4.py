from time import time


def func1():
    x = 999 ** 99999


def func2():
    L = [x for x in range(9999999)]


def func3():
    x = (66 * 9999) ** 99988


start_time = time()
func1()
end_time = time()
print(f'func1 took {end_time - start_time} seconds')

start = time()
func2()
end = time()
print(f'func2 took {end - start} seconds ')

start = time()
func3()
end = time()
print(f'func3 took {end - start} seconds')
