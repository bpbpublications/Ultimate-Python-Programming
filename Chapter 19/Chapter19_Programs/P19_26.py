L = [-3, 7, -9, 6, 3, 5, -8]
print(list(map(lambda x: x*x*x, filter( lambda x : x>0, L))))