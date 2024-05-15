trainees = {'12AB': {'name': 'Ash', 'experience': 12, 'language': 'C++'},
            '34CD': {'name': 'Dev', 'experience': 5, 'language': 'Python'},
            '55AB': {'name': 'Raj', 'experience': 10, 'language': 'C++'},
            '67CD': {'name': 'John', 'experience': 3, 'language': 'Java'},
            '23ED': {'name': 'Drek', 'experience': 7, 'language': 'Python'},
            '35ED': {'name': 'Amit', 'experience': 4, 'language': 'Python'}
            }
s = {rec['language'] for rec in trainees.values()}
print(s)
