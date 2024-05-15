search_string = input('Enter the text to be searched  : ')
with open('learn.txt', 'r') as f:
    for line in f:
        p = line.find(search_string)
        if p >= 0:
            print(line, end='')
