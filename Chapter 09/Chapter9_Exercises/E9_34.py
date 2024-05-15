pairs = []
for n1 in range(4):
    for n2 in range(4):
        if n1 != n2:
            pairs.append((n1, n2))
print(pairs)

pairs = [(n1, n2) for n1 in range(4) for n2 in range(4) if n1 != n2]
print(pairs)
