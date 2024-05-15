import random
from player import Player


def print_board(positions):
    number = 100
    for row in range(1, 11):
        if row % 2 != 0:  # odd rows 1,3,5...
            for i in range(number, number - 10, -1):
                print(f'{str(positions[i] if positions[i] is not None else i):>4}', end=' ')
            number -= 19
            print()
        else:  # even rows 2,4,6...
            for i in range(number, number + 10):
                print(f'{str(positions[i] if positions[i] is not None else i):>4}', end=' ')
            number -= 1
            print()
        print()


###########################################################################################################

colours = ['BLUE', 'GREEN', 'RED', 'YELLOW']

while True:
    n = int(input('How many players : '))
    if n in {2, 3, 4}:
        break
    print('You can have only 2,3 or 4 players')

players = []

for i in range(n):
    name = input(f'Enter name of player{i + 1}: ')
    colour = random.choice(colours)
    players.append(Player(name, colour))
    colours.remove(colour)

print()

for player in players:
    print(f'{player.name} gets {player.colour} coloured pawn')

print()

positions = [None for i in range(101)]

game_over = False

while not game_over:

    for player in players:  # each player's turn
        print_board(positions)
        print()

        current_position = player.place
        new_position = player.play()

        if new_position == 100:
            game_over = True
            break
        if new_position == current_position:  # cannot move situation
            continue

        if positions[new_position] is not None:  # someone is already present at the position
            for p in players:  # find the player who is at that position
                if p.colour[:3] == positions[player.place]:
                    print(f'Position occupied by {p.name}')
                    positions[p.place] = None
                    p.place = 0
                    print(f'{p.name} goes back to 0')
                    break

        positions[current_position] = None
        positions[new_position] = player.colour[:3]
