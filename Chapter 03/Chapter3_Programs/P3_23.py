s = '  hello      '
s = s.strip().upper().center(20, '*')
print(s)

s = '  hello      '
s = s.center(20, '*').upper().strip()
print(s)
