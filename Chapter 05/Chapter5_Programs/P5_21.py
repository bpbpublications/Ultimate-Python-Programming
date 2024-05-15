
from copy import deepcopy

office1_salary = {'manager': 6000,
                  'web designer': 3000,
                  'programmer': {'Python': 5000, 'Java': 4000, 'C#': 4500}
                  }

office2_salary = deepcopy(office1_salary)

office1_salary['programmer']['Python'] += 500

print(office1_salary)
print(office2_salary)

print(id(office1_salary['programmer']))
print(id(office2_salary['programmer']))
