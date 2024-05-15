s = 'Dev; 22; male; graduate; Bareilly'
print(s[s.index(';'):])
print(s[s.index(';') + 1:])

s2 = s[s.index(';') + 1:]
print(s2)

s2 = s[s.rindex(';') + 1:]
print(s2)

s2 = s[s.index(';') + 1: s.rindex(';')]
print(s2)

s2 = s[: s.find('xy')]
print(s2)

