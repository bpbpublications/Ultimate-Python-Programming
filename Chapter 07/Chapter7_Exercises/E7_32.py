s = '''A group of fearless rebels emerged, unafraid to be labelled as crazy or mad. 
Others called them mad troublemakers, but their insane ideas held the power to change the world. 
These visionaries proved that it is often the seemingly insane ones who hold the key to progress.'''

L = ['crazy', 'mad', 'rebels', 'lunatic', 'troublemakers', 'insane']

for word in L:
    s = s.replace(word, word[:1] + (len(word) - 1) * '*')

print(s)
