s = '''Focus on present, not on past or future
Focus on yourself, not on others
Focus on the process, not on outcome 
Focus on what you can control, not on what you cannot control'''

print(s.find('Focus'))
print(s.rfind('Focus'))
print(s.find('focus'))

print(s.count('on'))

print(s.startswith('Focus'))
print(s.endswith('?'))

print(s.find('Focus', 20, 100))