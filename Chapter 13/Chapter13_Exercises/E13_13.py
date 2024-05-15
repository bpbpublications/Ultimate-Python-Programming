with open('sample.py', 'r') as f:
    for line in f:
        if not line.startswith('#'):
            print(line, end='')
