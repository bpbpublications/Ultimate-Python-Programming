employee = ('Raj', 25, 'Delhi', 'raj@abc.com', 'XY289', 15000)

name, age, city, email, _, _ = employee
print(name, age, city, email)

name, _, city, email, _, salary = employee
print(name, city, email, salary)

name, dummy, city, email, dummy, salary = employee
print(name, city, email, salary)

