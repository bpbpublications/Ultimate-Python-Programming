with open('data.txt', 'r') as f:
    print(f.read())
    f.seek(0)
    print(f.read().lower())

