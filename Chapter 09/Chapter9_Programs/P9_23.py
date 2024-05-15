students = {'12AB': {'name': 'Raj', 'class': 5, 'marks': 400},
            '14XD': {'name': 'Dev', 'class': 6, 'marks': 350},
            '12YR': {'name': 'Rob', 'class': 4, 'marks ': 289},
            '13CP': {'name': 'Zen', 'class': 5, 'marks': 315},
            '23CX': {'name': 'Ted', 'class': 5, 'marks': 270},
            '15XG': {'name': 'Sam', 'class': 3, 'marks': 390},
            '19HY': {'name': 'Pam', 'class': 5, 'marks': 250},
            }
d = {id: 'Pass' if record['marks'] > 300 else 'Fail' for id, record in students.items() if record['class'] == 5}
print(d)
