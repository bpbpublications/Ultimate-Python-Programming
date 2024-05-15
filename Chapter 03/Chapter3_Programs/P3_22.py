s = '''Focus on present, not on past or future
Focus on yourself, not on others
Focus on the process, not on outcome 
Focus on what you can control, not on what you can't control'''

s2 = s.replace('Focus', 'Concentrate')
print(s2)
print()

s2 = s.replace('Focus', 'Concentrate', 3)
print(s2)
print()

s2 = s.replace('not', '')
print(s2)
print()

s2 = s.replace('not', '').replace('  ', ' ')
print(s2)
print()

