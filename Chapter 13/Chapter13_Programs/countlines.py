import sys

with open(sys.argv[1], 'r') as f:
    count = 0
    for line in f:
        count += 1
print(count)
