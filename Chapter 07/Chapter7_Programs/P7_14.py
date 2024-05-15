L = [('John', 20), ('Sam', 15), ('Dev', 21), ('Ryan', 10)]

for t in L:
    name, age = t
    if age > 18:
        print('Mr', name)
    else:
        print('Master', name)

for name, age in L:
    if age > 18:
        print('Mr', name)
    else:
        print('Master', name)

L = [['John', 20], ['Sam', 15], ['Dev', 21], ['Ryan', 10]]
for name, age in L:
    if age > 18:
        print('Mr', name)
    else:
        print('Master', name)
