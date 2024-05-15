import pickle
numbers = [10, 20, 30]
with open('data.pickle', 'wb') as file:
    pickle.dump(numbers, file)
