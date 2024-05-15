D = {'a': 23, 'd': 34, 'j': 56}
#val = D['b']  # Raises Error
val = D.get('b', 0)  # Returns 0
print(val)

val = D['b'] if 'b' in D else 0
print(val)