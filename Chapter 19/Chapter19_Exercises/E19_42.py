from functools import reduce

words = ['it', 'that', 'paper', 'won']

print(reduce(lambda s1, s2: s1 if len(s1) > len(s2) else s2, words))

print(max(words, key=len))
