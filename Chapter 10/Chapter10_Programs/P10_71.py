def func(a, b, c=1, d=2):
    print(a, b, c, d)

print(dir(func))

print(func.__name__)
fn = func
print(fn.__name__)
print(func.__module__)

from math import floor
print(floor.__module__)

print(func.__defaults__)

func.author = 'Ted'
func.creation_date = '9 Nov 2022'

print(dir(func))
print(func.author)
print(func.creation_date)




