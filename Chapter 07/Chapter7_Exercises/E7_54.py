text = 'It is often the seemingly insane ones who hold the key to progress'
prohibited_words = ['mad', 'insane', 'crazy']

for s in text.split():
    if s in prohibited_words:
        print('Found a prohibited word')
        break
else:
    print('No prohibited word in the list')
