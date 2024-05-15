names = ['John', 'Sam', 'Marie', 'Anne']
login = dict.fromkeys(names, None)
print(login)

designation = ['programmer', 'manager', 'accountant']
salary = [4000, 5000, 3000]
D = dict(zip(designation, salary))
print(D)
