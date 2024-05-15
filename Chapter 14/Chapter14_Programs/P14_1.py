class Person:
    pass


print(id(Person))
print(type(Person))

p1 = Person()
p2 = Person()

print(type(p1))
print(type(p2))
print(id(p1))
print(id(p2))

