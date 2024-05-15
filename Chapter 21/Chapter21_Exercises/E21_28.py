class ListProtector:
    def __init__(self, original_list):
        self.original = original_list

    def __enter__(self):
        self.copy_of_list = self.original.copy()
        return self.copy_of_list

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.original[:] = self.copy_of_list
        else:
            print('Error while working on the list, any changes to the list are discarded.')
        return True


mylist = [10, 20, 30]

with ListProtector(mylist) as working_mylist:
    working_mylist.append(40)
    working_mylist.append(20 + 100)

print(mylist)

with ListProtector(mylist) as working_mylist:
    working_mylist.append(60)
    working_mylist.append(34)
    working_mylist.append(20 / 0)

print(mylist)
