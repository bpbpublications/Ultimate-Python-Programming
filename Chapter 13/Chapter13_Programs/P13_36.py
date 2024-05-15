def append(file1, *args):
    with open(file1, 'r') as f1:
        for file in args:
            with open(file, 'a') as f2:
                for line in f1:
                    f2.write(line)
            f1.seek(0)


append('copyright.txt', 'document1.txt', 'document2.txt')
append('companyinfo.txt', 'file1.txt', 'file2.txt', 'file3.txt', 'file4.txt')
