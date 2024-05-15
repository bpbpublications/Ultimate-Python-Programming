schools = [('XYZ', 1, 2), ('PQR', 9, 8), ('ABC', 9, 0), ('LMN', 8, 7)]

for school_name, boys, girls in schools:
    ratio = boys / girls
    print(f'Ratio of boys to girls for school {school_name} is {ratio}')
    if ratio > 1:
        print('Boys in majority\n')
    else:
        print('Girls in majority\n')
