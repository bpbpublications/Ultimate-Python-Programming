def result(name, standard, *args):
    total = sum(args)
    print(f'{name},{standard}, Total Marks = {total}')


result('Anu', 80, 95, 76, standard='V')
