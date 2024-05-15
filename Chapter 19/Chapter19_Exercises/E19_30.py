L = ['spam', '', 'ten', '', 'run']

T = tuple(filter(lambda x: x != '', L))
print(T)

T = tuple(filter(None, L))
print(T)

T = tuple(x for x in L if x != '')
print(T)
