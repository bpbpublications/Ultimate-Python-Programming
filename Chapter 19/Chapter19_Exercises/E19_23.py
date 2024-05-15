names = [('Aman', 'Kumar'), ('Kamal', 'Kapoor'), ('Kamal', 'Gupta'), ('Raj', 'Kumar')]
L = sorted(names, key=lambda x: x[1][::-1])
print(L)
