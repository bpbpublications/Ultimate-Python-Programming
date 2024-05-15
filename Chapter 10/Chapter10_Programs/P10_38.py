def result(total, sports=None, arts=None):
    print('Total marks = ', total)
    if sports is not None:
        print('Sports Grade', sports)
    if arts is not None:
        print('Arts Grade', arts)


result(98, 'A')
result(78, 'B', 'C')
result(88)
