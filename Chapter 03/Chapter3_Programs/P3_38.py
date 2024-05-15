name = 'Raj'
age = 23
wt = 47.567
s = 'My name is {}, I am {} years old and my weight is {} kg'.format(name, age, wt)
print(s)

s = 'My name is {0}, I am {1} years old and my weight is {2} kg'.format(name, age, wt)
print(s)

s = 'Age {1} years, Name {0}, weight {2} kg, bye from {0}'.format(name, age, wt)
print(s)

s = '{msg}, my name is {n}, I am {a} years old'.format(n=name, a=age, msg='Hello')
print(s)

s = '{msg}, I am {1} years old and my weight is {0} kg'.format(wt, age, msg='Hello')
print(s)



