def subtract(a, b):
    print(a - b)

def add(a, b):
    print(a + b)

def multiply(a, b):
    print(a * b)

def divide(a, b):
    print(a // b)

def calculate(fn, a1, a2):
    fn(a1, a2)

calculate(add, 5, 2)
calculate(subtract, 5, 2)

