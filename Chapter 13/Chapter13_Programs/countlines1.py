import sys
if len(sys.argv) == 1:
    filename = input('Enter filename : ')
else:
    filename = sys.argv[1]

with open(filename, 'r') as f:
    count = 0
    for line in f:
       count += 1
print(count)
