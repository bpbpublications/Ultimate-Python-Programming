searchname = input('Enter the name to be searched : ')

with open('students_info.txt','r') as f:
    for line in f:
        name, *_ = line.split(':')
        if name.strip().lower() == searchname.lower():
            print(line)

