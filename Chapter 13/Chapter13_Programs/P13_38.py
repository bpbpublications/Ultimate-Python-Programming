with open('info.txt', 'r') as f:
    lines = [line.rstrip() for line in f if line[0].isdigit()]
    print(lines)

