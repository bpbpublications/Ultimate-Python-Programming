def months_of_year():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
              'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    i = 0
    while True:
        yield months[i]
        i = (i + 1) % 12


g = months_of_year()

for i in range(20):
    print(next(g), end=' ')
