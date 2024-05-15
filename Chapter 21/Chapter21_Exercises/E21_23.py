def file_compare(file1, file2):
    with open('test.txt', 'r') as f1, open('test1.txt', 'r') as f2:
        line_number = 1
        while True:
            line1 = f1.readline().strip()
            line2 = f2.readline().strip()
            if line1 != line2:
                print('Line : ', line_number)
                print(file1, line1)
                print(file2, line2)
            if line1 == '' and line2 == '':
                break
            line_number += 1


file_compare('test.txt', 'test1.txt')
