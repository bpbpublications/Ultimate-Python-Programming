from itertools import cycle, islice
fruits = cycle(['Apple', 'Mango', 'Banana', 'Grapes'])

for x in islice(fruits,5,10):
    print(x, end=' ')



