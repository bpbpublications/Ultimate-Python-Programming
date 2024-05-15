data = 'Amit:20,Sumit:30,Namit:34,Dev:23,Ankur:32'
D = {}
for pair in data.split(','):
    pair = pair.split(':')
    D[pair[0]] = int(pair[1])
print(D)

