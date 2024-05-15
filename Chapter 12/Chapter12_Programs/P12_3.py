x = 3

def func(a):
    y = 10
    print(locals())
    
func(5)
print(globals())
import prime
from words import *
print(globals())
