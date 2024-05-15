items = {'x': 100, 'y': 50, 'z': 90, 'd': 67}

if any(p > 100 for p in items.values()):
    print('Not everything is affordable')
else:
    print('Everything is affordable')
