blank_lines = 0
with open('info.txt', 'r') as f:
    for line in f:
        if line.strip() == '':
            blank_lines += 1
print(blank_lines)
