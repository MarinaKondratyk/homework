from random import randint

WIN = {'stone': 'scissors', 'scissors': 'paper', 'paper': 'stone'}


def players() -> str:
    n = list(WIN.values())[randint(0, 2)]
    print(n)
    return n


def game(player_1: str, player_2: str) -> str:
    while player_1 == player_2:
        return game(players(), players())
    else:
        if player_2 in WIN[player_1]:
            return f'Winner is {player_1}'
        else:
            return f'Winner is {player_2}'


print(game(players(), players()))