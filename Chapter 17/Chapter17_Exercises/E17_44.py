def max_limit(data, maximum):
    for item in data:
        if item < maximum:
            yield item


def min_limit(data, minimum):
    for item in data:
        if item > minimum:
            yield item


L = [2, 8, 4, 1, 5, 6, 7, 9]

d = {'a': 5, 'b': 4, 'c': 5, 'd': 2, 'e': 9}

print(sum(max_limit(L, 5)), end='  ')
print(sum(min_limit(d.values(), 4)))
