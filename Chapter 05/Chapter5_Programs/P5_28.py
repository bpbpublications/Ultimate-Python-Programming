python_programmers = {'Nick', 'Sam', 'Peter', 'Mary', 'Alan', 'Rose', 'Zara', 'Max'}
java_programmers = {'Ted', 'Sandy', 'Peter', 'Alan', 'Ross', 'Max', 'Ruby'}
c_programmers = {'Nick', 'Ted', 'Peter', 'Abbie', 'Julie', 'Jack', 'Jill'}

print(python_programmers.intersection(java_programmers))
print(python_programmers & java_programmers)

print(python_programmers.intersection(java_programmers, c_programmers))
print(python_programmers & java_programmers & c_programmers)

print(c_programmers.union(python_programmers))
print(c_programmers | python_programmers)

print(python_programmers - java_programmers)
print(python_programmers.difference(java_programmers))

print(python_programmers.difference(java_programmers, c_programmers))
print(python_programmers - java_programmers- c_programmers)

print(python_programmers.symmetric_difference(java_programmers))
print(python_programmers ^ java_programmers)

python_programmers.intersection_update(java_programmers)
print(python_programmers)

java_programmers &= c_programmers
print(java_programmers)
