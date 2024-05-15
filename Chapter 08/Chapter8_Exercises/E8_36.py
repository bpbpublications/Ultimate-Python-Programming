names1 = ['Sam', 'Rob', 'Fed', 'Tim']
names2 = ['John', 'Kim', 'Rob', 'Fed', 'Jim']
for name in names1[:]:
    if name in names2:
        names1.remove(name)
print(names1)
