with open('data.txt', 'r') as f1, open('new.txt', 'w') as f2:
    s = f1.read()
    f2.write(s)

with open('new.txt', 'r') as f:
    print(f.read())