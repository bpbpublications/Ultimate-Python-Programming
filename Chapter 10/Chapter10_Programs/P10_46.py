def func(name, title='developer', salary=3000):
    print(f'{name} is a {title} and gets {salary}')

func('Mark')
func('Mark', 'programmer')
func('Mark', 'programmer', 4000)

func(name='Mark')
func(name='Mark', title='programmer')
func(name='Mark', title='programmer', salary=4000)

