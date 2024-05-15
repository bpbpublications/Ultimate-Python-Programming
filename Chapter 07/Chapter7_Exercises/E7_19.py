D = {'Mark': 25, 'Tom': 65, 'John': 37, 'Rob': 45}
for name, age in D.items():
    if age > 65:
        print(name)
        break
else:
    print('No senior citizens')
