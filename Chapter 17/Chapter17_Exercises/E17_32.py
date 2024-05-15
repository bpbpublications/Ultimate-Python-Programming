def generate_squares(start, stop):
    while start <= stop:
        yield start * start
        start += 1


g = generate_squares(2, 9)

for i in g:
    print(i)
