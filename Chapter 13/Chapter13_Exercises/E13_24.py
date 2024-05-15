import os

with open('myfile.py', 'r') as f1:
    with open('new.py', 'w') as f2:
        for line in f1:
            if not line.startswith('#'):
                f2.write(line)
os.remove('myfile.py')
os.rename('new.py', 'myfile.py')
