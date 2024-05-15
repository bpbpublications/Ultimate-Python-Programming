print(all([1, 2, 3, 0, 5, 8]))
print(all([1, 2, 3, 5, 8]))

names = ['Raj', 'Dev', '', 'Sam']
print(all(names))

marks = [65, 67, 89, 48, 90, 56]
print(all(m > 50 for m in marks) )

marks.remove(48)
print(all(m > 50 for m in marks) )

print(any(m > 100 for m in marks))

marks.insert(2, 150)
print(any(m > 100 for m in marks))





