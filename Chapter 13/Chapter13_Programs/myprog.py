with open('myfile1.txt','r', encoding='utf-8') as f:
    f.seek(4)
    print(f.read())

with open('myfile2.txt','r', encoding='utf-8') as f:
    f.seek(3)
    print(f.read())
