import pickle
names = ['John', 'Bob', 'Tom']
data = {'a':1, 'b':2, 'c':3}
numbers = [10, 20, 30]

with open('data.pickle', 'wb') as file:
    pickle.dump((numbers, names, data), file)
