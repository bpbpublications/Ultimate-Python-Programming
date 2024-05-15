with open('names.txt', 'r') as f:
    for line in reversed(f.readlines()):
        print(line, end='')

