from itertools import count

it = count(start=10, step=3)
print(next(it), next(it), next(it))
print(next(it), next(it), next(it))

for i in count(10, 3):
    if i > 30:
        break
    print(i)
