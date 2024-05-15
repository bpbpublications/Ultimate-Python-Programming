f = open('data.txt', 'r')
lines = (line for line in f if line != '\n')

print(next(lines), end='')
print(next(lines), end='')
print(next(lines), end='')

f.close()
