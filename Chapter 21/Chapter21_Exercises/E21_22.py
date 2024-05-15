with open('data.txt', 'r') as f1:
    with open('new.txt', 'w') as f2:
        for line in f1:
            f2.write(line + '\n')

with open('data.txt', 'r') as f1, open('new.txt', 'w') as f2:
    for line in f1:
        f2.write(line + '\n')
