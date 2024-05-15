with (
    open('data.txt', 'r') as f1,
    open('new.txt', 'w') as f2,
    open('test1.txt', 'w') as f3,
):
    for line in f1:
        f2.write(line + '\n')
        f3.write(line + '\n')
