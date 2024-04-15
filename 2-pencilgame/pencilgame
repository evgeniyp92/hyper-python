import random

def draw_pencils(n):
    for i in range(n):
        print('|', end='')
    print()


players = ['Eugene', 'Jolene']
players_names = ', '.join(players)

num_pencils = 0

print("How many pencils would you like to use")
while num_pencils == 0:
    num_pencils_candidate = input()
    try:
        num_pencils_candidate = int(num_pencils_candidate)
        if int(num_pencils_candidate) <= 0:
            print("The number of pencils should be positive")
            continue
        num_pencils = num_pencils_candidate
    except ValueError:
        print("The number of pencils should be numeric")
        continue

player = ''
print(f'Who will go first ({players_names}):')
player_input = input()
while player_input not in players:
    print("Choose between 'Eugene' and 'Jolene'")
    player_input = input()
player = player_input

while num_pencils > 0:
    draw_pencils(num_pencils)
    print(f"{player}'s turn:")
    num_pencils_to_remove = 0
    if player == 'Eugene':
        # Human input
        valid_input = False
        while not valid_input:
            try:
                num_pencils_to_remove = int(input())
                if num_pencils_to_remove <= 0 or num_pencils_to_remove >= 4:
                    raise ValueError
                if num_pencils_to_remove > num_pencils:
                    print('Too many pencils were taken')
                    continue
            except ValueError:
                print("Possible values: '1', '2' or '3'")
                continue
            valid_input = True
            num_pencils -= num_pencils_to_remove
    else:
        # Bot
        if (num_pencils - 1) % 4 == 0:
            # Losing position
            if num_pencils == 1:
                num_pencils_to_remove = 1
            else:
                num_pencils_to_remove = random.randint(1, 3)
        else:
            # Winning position
            if num_pencils % 4 == 0:
                num_pencils_to_remove = 3
            elif (num_pencils + 1) % 4 == 0:
                num_pencils_to_remove = 2
            else:
                num_pencils_to_remove = 1
        print(num_pencils_to_remove)
        num_pencils -= num_pencils_to_remove
    if num_pencils == 0:
        print(f'{"Eugene" if players.index(player) == 1 else "Jolene"} has won the game!')
        break
    player = 'Eugene' if players.index(player) == 1 else 'Jolene'
