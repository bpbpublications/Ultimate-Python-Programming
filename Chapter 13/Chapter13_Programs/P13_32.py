with open('new.txt', 'w') as f1, open('names.txt', 'r') as f2:
    f1.write(f2.read())
