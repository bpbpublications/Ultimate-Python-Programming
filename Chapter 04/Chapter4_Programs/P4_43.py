
employee = ('Raj', 25, 'Delhi', 'raj@abc.com', 'XY289', 15000)
name, *_, salary = employee
print(name, salary)

name, *skip, salary = employee
print(name, salary)

record = ('Ted', 25, 'Paris', 'Java', 'C++', 'C', 'Python')
name, age, city, *languages = record
print(name, age, city, languages)

author = ('Learn C', 'Python Programming', 'Data structures', 'Alex', 'alex@gmail.com')
*books, name, email = author
print(books, name, email)