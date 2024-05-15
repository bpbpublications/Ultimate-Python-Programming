def func(name, title, salary):
    print(f'{name} is a {title} and gets {salary}')


func('Nick', 'manager', 5000)

func(name='Nick', title='manager', salary=5000)
func(title='manager', salary=5000, name='Nick')
func(title='manager', name='Nick', salary=5000)

func('Nick', salary=5000, title='manager')
func('Nick', 'manager', salary=5000)
