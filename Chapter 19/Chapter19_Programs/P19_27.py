L1 = ['??', 'abc', 'Efg', '123', 'A1', 'pqr']
print(list(map(str.upper, filter(lambda s : s.isalpha(), L1))))