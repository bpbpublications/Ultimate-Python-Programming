L = [lambda s: s.strip().lower(),
     lambda s: s.strip().upper(),
     lambda s: s.lstrip().title(),
     lambda s: s[::-1].lower(),
     ]
print(L[1]('Python'))

print(L[3]('Python'))
