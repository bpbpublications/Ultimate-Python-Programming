print(min(-5, 2, -34, key=abs))

def absolute(n):
    return -n if n < 0 else n

print(min(5, 2, -34, key=absolute))
