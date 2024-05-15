d = {'Poems for kids': 'Joe',
     'Stories for kids': 'Zen',
     'Health is wealth': 'James',
     'Rhymes for Babies': 'Joe',
     'Stories for teens': 'Ted',
     'Be healthy': 'James'
     }

d1 = {value: key for key, value in d.items()}
print(d1)

d2 = {value: [x for x,y in d.items() if y==value ] for key,value in d.items()}
print(d2)

d3 = {value: [x for x, y in d.items() if y == value] for value in set(d.values())}
print(d3)
