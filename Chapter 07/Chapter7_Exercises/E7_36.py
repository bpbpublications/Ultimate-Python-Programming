names = {'_num', 'var', 'product', '_add', '_sub', 'square'}
x = set()
for name in names:
    if name.startswith('_'):
        x.add(name)
print(x)
