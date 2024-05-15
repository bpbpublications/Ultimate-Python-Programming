with open('data.txt', 'r') as f1:
    with open('new.txt', 'w') as f2:
        f2.write(f1.read().replace(' ', '-'))
