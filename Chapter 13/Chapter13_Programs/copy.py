import sys

with open(sys.argv[1], 'w') as f1, open(sys.argv[2], 'r') as f2:
    for line in f2:
        f1.write(line)
