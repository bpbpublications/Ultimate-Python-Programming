names = ['Sam', 'Ted', 'Joe', 'Max']
marks = [90, 98, 78, 89]

d = {key: value for key, value in zip(names, marks)}
print(d)
