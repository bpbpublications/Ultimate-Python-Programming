toppers = {'id11', 'id23', 'id34', 'id45', 'id77', 'id12', 'id89', 'id56', 'id55', 'id19'}
champions = {'id19', 'id23', 'id78', 'id99', 'id79', 'id13', 'id56', 'id45', 'id80'}

toppers.remove('id11')
print(toppers)
toppers.add('id46')
toppers.add('id20')
print(toppers)

print(toppers - champions)
print(champions - toppers)
print(toppers & champions)
print(toppers | champions)

