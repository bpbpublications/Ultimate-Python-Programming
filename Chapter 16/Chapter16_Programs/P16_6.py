class Person:
    pass

print(issubclass(Person, object))

class Person1(object):
    pass

print(issubclass(Person1, object))

print(issubclass(str, object))
print(issubclass(int, object))
print(issubclass(dict, object))

