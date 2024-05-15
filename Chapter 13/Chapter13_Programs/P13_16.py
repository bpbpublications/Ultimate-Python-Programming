with open('mydata.txt', 'r', encoding='utf-8') as f:
    while True:
        part = f.read(10)
        if part == '':
            break
        print(part, end='')
