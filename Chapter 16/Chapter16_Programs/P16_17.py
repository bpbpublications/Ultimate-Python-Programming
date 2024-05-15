class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        self.draw_current()
        self.spin()
        self.ignite()

    def draw_current(self):
        print('Drawing current')

    def spin(self):
        print('Spinning')

    def ignite(self):
        print('Igniting')


class Brakes:
    def __init__(self, weight):
        self.weight = weight

    def activate(self):
        print('Activating brakes')

    def release(self):
        print('Releasing brakes')


class Car:
    def __init__(self, name, engine, brakes):
        self.name = name
        self.engine = engine
        self.brakes = brakes

    def start(self):
        self.engine.start()

    def stop(self):
        self.brakes.activate()


e = Engine(120)
b = Brakes(5)
car = Car('Breeze', e, b)
car.start()
car.stop()
