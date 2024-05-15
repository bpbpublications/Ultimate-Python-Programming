with open('names.txt', 'r') as f:
    count = 0
    for line in f:
        count += 1
        print(count, line, end='')
