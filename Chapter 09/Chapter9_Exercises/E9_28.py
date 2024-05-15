d = {'India': 'Rupee',
     'UK': 'Pound',
     'France': 'Euro',
     'Japan': 'Yen',
     'Austria': 'Euro',
     'Bangladesh': 'Taka',
     'Italy': 'Euro'
     }

for country, currency in d.items():
    if currency == 'Yen':
        print(country)
        break

print([country for country, currency in d.items() if currency == 'Euro'])
