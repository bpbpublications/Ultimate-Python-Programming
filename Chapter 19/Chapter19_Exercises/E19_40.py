s = 'abc,(1,2,3),[9,10],(5,3)'

print(set(filter(lambda ch: not ch.isalnum(), s)))

print(set(ch for ch in s if not ch.isalnum()))
