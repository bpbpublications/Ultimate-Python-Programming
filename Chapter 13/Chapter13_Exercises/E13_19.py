with open('info1.txt', 'r') as f1:
    with open('info2.txt', 'r') as f2:
        count = 1
        while True:
            line1 = f1.readline()
            line2 = f2.readline()
            if line1 == '' and line2 == '':
                break
            if line1 != line2:
                print('Line ', count)
                print(line1, end='')
                print(line2)
            count += 1
