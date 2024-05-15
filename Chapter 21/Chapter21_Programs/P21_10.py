import sys

print('Welcome')

numbers = [1, 2, 3, 4]
print(numbers)
print(numbers * 2)

print('Redirecting Output to test.txt.....')
f = open('test.txt', 'a')
original = sys.stdout
sys.stdout = f

for n in numbers:
    print(sum(range(1, n + 1)), end=' ')
print()
print([x * 100 for x in numbers])

sys.stdout = original
f.close()
print('Output prints to screen now.....')

d = {61: 'a', 32: 'b', 31: 'c'}
print(d)
print(sorted(d.keys()))

s1 = {'x', 'a', 'b'}
s2 = {'x', 'a', 'b', 'c', 'd'}
print(s1 | s2)
print(s2 - s1)

print(2 + 3 * 5)
print('Bye')
