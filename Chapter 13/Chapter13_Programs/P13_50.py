import pickle

with open('data.pickle', 'rb') as file:
    a = pickle.load(file)
    b = pickle.load(file)
    c = pickle.load(file)
print(type(a), type(b), type(c))
print(a, b, c)
