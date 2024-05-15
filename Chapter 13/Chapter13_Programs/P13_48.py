import pickle
with open('data.pickle', 'rb') as file:
    a, b, c = pickle.load(file)
print(a, b, c)
