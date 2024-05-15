L1 = ['China', 'Brazil', 'India', 'Iran', 'Iraq', 'Russia']
L2 = ['Italy', 'Japan', 'China', 'Russia', 'Nepal', 'France']
L3 = []
for i in L1:
    for j in L2:
        if i == j:
            L3.append(i)
print(L3)

# Can also write it by using the in operator.

L3 = []
for i in L1:
    if i in L2:
        L3.append(i)
print(L3)
