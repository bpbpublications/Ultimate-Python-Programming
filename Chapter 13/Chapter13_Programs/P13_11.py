with open('time.txt', 'w') as fout:
    fout.write('Time is precious')

print(fout.closed)

with open('time.txt', 'r') as fin:
    s = fin.read()
    print(s)

print(fin.closed)
