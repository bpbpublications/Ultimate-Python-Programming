import random

ladders = {3: 34, 9: 14, 12: 96, 20: 42, 32: 51, 37: 65, 63: 99, 69: 90}

snakes = {15: 2, 31: 10, 34: 24, 40: 25, 81: 43, 84: 57, 87: 55, 92: 18}


class Player:

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.place = 0

    def _roll_dice(self):
        input(f'\n{self.name}({self.colour}), Press Enter to roll the dice')
        roll = random.randint(1, 6)
        print(f'You rolled a {roll},', end=' ')
        return roll

    def play(self):

        while True:
            roll = self._roll_dice()

            if self.place + roll > 100:
                print(f'You cannot move, you need to roll a {100 - self.place} to win\n')
                return self.place

            self.place += roll
            print(f'You move to square {self.place}\n')

            if self.place == 100:
                print(f'Game over ... {self.name} wins')
                return self.place
            elif self.place in ladders.keys():
                print('You landed on a ladder,', end=' ')
                self.place = ladders[self.place]
                print(f'Climb to {self.place}\n')
            elif self.place in snakes.keys():
                print(f'You landed on a snake,', end=' ')
                self.place = snakes[self.place]
                print(f'Move down to {self.place}\n')
            else:
                pass

            if roll == 6:
                print('You get another chance for rolling a 6')
                continue

            return self.place
