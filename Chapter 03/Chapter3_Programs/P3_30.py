name = 'Raj'
age = 23
wt = 47.5
s = 'My name is %s, I am %d years old and my weight is %f kg' % (name, age, wt)
print(s)

s = 'My name is {}, I am {} years old and my weight is {} kg'.format(name, age, wt)
print(s)

s = f'My name is {name}, I am {age} years old and my weight is {wt} kg'
print(s)
