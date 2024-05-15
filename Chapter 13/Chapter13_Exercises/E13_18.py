with open('info1.txt', 'r') as f1:
    with open('info2.txt', 'r') as f2:
        count = 1
        while True:
            line1 = f1.readline()
            line2 = f2.readline()
            if line1 != line2:
                print('Files differ at line', count)
                break
            if line1 == '':
                print('Files are same')
                break
            count += 1
