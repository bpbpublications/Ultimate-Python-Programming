def average(*args):
    return sum(args) / len(args)


a1 = average(9, 2, 1)
a2 = average(3, 5, 6, 7, 8)

L = [1, 5, 7, 8, 0, 4, 2, 8, 5]
a3 = average(*L)

d = {'John': 23, 'Ted': 25, 'Sam': 27, 'Nick': 21}
a4 = average(*d.values())

print(a1, a2, a3, a4)
