with open('new.txt', 'a') as f1, open('names.txt', 'r') as f2:
    for line in f2:
        f1.write(line)
