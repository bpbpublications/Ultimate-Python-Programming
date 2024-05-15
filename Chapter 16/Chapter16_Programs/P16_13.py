class Car:
    def start(self):
        print('Engine started')

    def move(self):
        print('Car is running')

    def stop(self):
        print('Brakes applied')


class Clock:
    def move(self):
        print('Tick Tick Tick')

    def stop(self):
        print('Clock needles stopped')


class Person:
    def move(self):
        print('Person walking')

    def stop(self):
        print('Taking rest')

    def talk(self):
        print('Hello')

def do_something(x):
   x.move()
   x.stop()

car = Car()
clock = Clock()
person = Person()
do_something(car)
do_something(clock)
do_something(person)
