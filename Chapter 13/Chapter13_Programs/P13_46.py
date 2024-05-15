import pickle
with open('data.pickle', 'rb') as file:
    a = pickle.load(file)
print(type(a))
print(a)
