def append(file1, *args):
    with open(file1, 'r') as f1:
        text = f1.read()

    for file in args:
        with open(file, 'a') as f2:
            f2.write(text)


append('copyright.txt', 'document1.txt', 'document2.txt')
append('companyinfo.txt', 'doc1.txt', 'doc2.txt', 'doc3.txt', 'doc4.txt')
