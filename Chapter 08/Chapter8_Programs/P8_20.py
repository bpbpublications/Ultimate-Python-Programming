pronouns = {'me', 'they', 'everybody', 'those', 'he', 'myself', 'it'}
for word in pronouns:
    if len(word) > 4:
        pronouns.remove(word)
print(pronouns)
