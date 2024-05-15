class OutOfRangeError(Exception):
    '''Exception raised when a value is out of acceptable range'''

    def __init__(self, name, minValue, maxValue):
        self.name = name
        self.minValue = minValue
        self.maxValue = maxValue

    def __str__(self):
        return f'{self.name} should be between {self.minValue} and {self.maxValue}'


try:
    age = int(input('Enter age : '))
    if age < 18 or age > 60:
        raise OutOfRangeError(name='age', minValue=18, maxValue=60)

    salary = int(input('Enter salary : '))
    if salary < 10000 or salary > 500000:
        raise OutOfRangeError('salary', 10000, 50000)
except OutOfRangeError as e:
    print(e)
