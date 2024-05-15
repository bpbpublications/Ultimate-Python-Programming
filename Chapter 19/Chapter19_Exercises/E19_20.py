def f(s1, s2):
    return lambda text: s1 + ', ' + text + ' ' + s2


f1 = f('Dear Sir', 'Thankyou')
f2 = f('Sir/Madam', 'Thanks')
f3 = f('Hi', 'Bye')

print(f1('Please contact me.'))
print(f2('Please respond.'))
print(f3('How are you?'))
print(f3('Where are you?'))
