L = ['Cow', 'Zebra', 'Ant', 'bat', 'crow', 'Wolf']
L.sort()
print(L)

L = ['Cow', 'Zebra', 'Ant', 'bat', 'crow', 'Wolf']
L.sort(key=str.lower)
print(L)

L = ['Cow', 'Zebra', 'Ant', 'bat', 'crow', 'Wolf']
L.sort(key=str.upper)
print(L)

L = ['Cow', 'Zebra', 'Ant', 'bat', 'crow', 'Wolf']
L.sort(key=len)
print(L)