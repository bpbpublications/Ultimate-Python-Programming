def copy_file(source, destination):
    with open(source, 'r') as f1, open(destination, 'w') as f2:
        while True:
            s = f1.read(100)
            if s == '':
                break
            f2.write(s)


copy_file('data.txt', 'data1.txt')
