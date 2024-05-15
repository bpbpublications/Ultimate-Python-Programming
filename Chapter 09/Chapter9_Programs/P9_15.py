d = {'Poems for kids': 'Joe',
     'Stories for kids': 'Zen',
     'Health is wealth': 'James',
     'Rhymes for Babies': 'Joe',
     'Stories for teens': 'Ted',
     'Be healthy': 'James'
     }

L1 = [book_name for book_name, author in d.items() if author == 'James']
print(L1)
