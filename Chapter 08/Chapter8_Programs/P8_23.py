names = []
name = ''
while name != 'exit':
    name = input('Enter name : ')
    names.append(name)
print(names)

names = []
name = ''
while name != 'exit':
    name = input('Enter name : ')
    if name != 'exit':
        names.append(name)
print(names)

names = []
while True:
    name = input('Enter name : ')
    if name == 'exit':
        break
    names.append(name)
print(names)

