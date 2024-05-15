import pickle

with open('students.pickle', 'rb') as file:
    d = pickle.load(file)
    print(d)
