with open('data.txt', 'r') as f:
    for line in f.readlines()[-5::]:
        print(line, end='')
