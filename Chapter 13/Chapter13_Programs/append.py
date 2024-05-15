import sys

with open(sys.argv[1], 'a') as f1:
    for file in sys.argv[2:]:
        with open(file, 'r') as f2:
            for line in f2:
                f1.write(line)
