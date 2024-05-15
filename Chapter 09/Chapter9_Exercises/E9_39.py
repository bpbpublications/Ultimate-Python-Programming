names = ['Ted', 'Sam', 'Jim', 'Rob', 'Anu']
maths = [98, 67, 54, 88, 95]
physics = [88, 64, 78, 99, 78]
chemistry = [78, 67, 45, 79, 87]

d = {name: {'Maths': m1, 'Physics': m2, 'Chemistry': m3} for name, m1, m2, m3 in zip(names, maths, physics, chemistry)}

print(d)
