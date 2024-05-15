import os

search_string = 'This'

for name in os.listdir('.'):
    if os.path.isfile(name):
        print('Searching file ', name)
        with open(name, 'r') as f:
            for line in f:
                p = line.find(search_string)
                if p >= 0:
                    print(line, end='')
        print()
