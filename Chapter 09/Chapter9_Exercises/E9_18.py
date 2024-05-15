names = ['ted williams', 'John smith', 'tim jones']
names = [name.title() for name in names]
print(names)

names = ['ted williams', 'John smith', 'tim jones']
for name in names:
    name = name.title()
print(names)

names = ['ted williams', 'John smith', 'tim jones']
for i in range(len(names)):
    names[i] = names[i].title()
print(names)
