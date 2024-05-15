s1 = 'Abc'
s2 = 'XYz'
L = []
for ch1 in s1:
    for ch2 in s2:
        L.append(ch1 + ch2)
print(L)

L1 = [ch1 + ch2 for ch1 in s1 for ch2 in s2]
print(L1)

L2 = [ch1 + ch2 for ch1 in s1 if ch1.islower() for ch2 in s2 if ch2.isupper()]
print(L2)

L3 = []
for ch1 in s1:
    if ch1.islower():
        for ch2 in s2:
            if ch2.isupper():
                L3.append(ch1 + ch2)
print(L3)
