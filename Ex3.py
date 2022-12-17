#Создайте программу для игры в ""Крестики-нолики"".

from time import sleep
from random import shuffle, randint

win_rules = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 5, 9),
    (3, 5, 7),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
)
turns = {i: str(i) for i in range(1, 10)}
def_symbol = 'x'


def draw_field():
    print('—' * 13)
    for j in range(1, 9, 3):
        for i in range(j, 3 + j):
            if turns[i] == 'x':
                print(f'| \033[1;31m{turns[i]} \033[0m', end='')
            elif turns[i] == 'o':
                print(f'| \033[1;32m{turns[i]} \033[0m', end='')
            else:
                print(f'| \033[01;38;05;252m{i}\033[0m ', end='')
        print('|\n', '—' * 13)


def change_symbol():
    global def_symbol
    if def_symbol == 'x':
        def_symbol = 'o'
    else:
        def_symbol = 'x'


def get_opp_symbol():
    if def_symbol == 'x':
        return 'o'
    else:
        return 'x'


def bot_logic():
    if turns[5].isdigit():
        return 5
    else:
        corners = [1, 3, 7, 9]
        shuffle(corners)
        for line in win_rules:
            if turns[line[0]] == turns[line[1]] == def_symbol and turns[line[2]].isdigit():
                return line[2]
            if turns[line[0]] == turns[line[2]] == def_symbol and turns[line[1]].isdigit():
                return line[1]
            if turns[line[1]] == turns[line[2]] == def_symbol and turns[line[0]].isdigit():
                return line[0]
        for line in win_rules:
            if turns[line[0]] == turns[line[1]] == get_opp_symbol() and turns[line[2]].isdigit():
                return line[2]
            if turns[line[0]] == turns[line[2]] == get_opp_symbol() and turns[line[1]].isdigit():
                return line[1]
            if turns[line[1]] == turns[line[2]] == get_opp_symbol() and turns[line[0]].isdigit():
                return line[0]
        for pos in corners:
            if turns[pos].isdigit():
                return pos
        while True:
            tmp = randint(1, 9)
            if turns[tmp].isdigit():
                return tmp


def bot_turn():
    bt = bot_logic()
    turns[bt] = def_symbol
    print(f'Бот выбрал позицию {bt}')
    if is_win():
        print(def_symbol, 'выиграл.')
        exit()
    if not is_continue():
        print('Ничья')
        exit()
    change_symbol()


def is_win():
    for line in win_rules:
        if turns[line[0]] == turns[line[1]] == turns[line[2]]:
            print(turns[line[0]], 'выиграл.')
            draw_field()
            return True
    return False


def is_continue():
    for i in turns.values():
        if i.isdigit():
            return True
    return False


def pos_input():
    while True:
        try:
            num = int(input(f'Введите позицию {def_symbol}: '))
            if 0 < num < 10 and turns[num].isdigit():
                return num
            else:
                print('Такой позиции нет или она занята, введите заново')
        except ValueError:
            print('Введите целое число')


def player_turn():
    draw_field()
    n = pos_input()
    turns[n] = def_symbol
    change_symbol()
    if is_win():
        print(def_symbol, 'выиграл.')
        exit()
    if not is_continue():
        print('Ничья')
        exit()


who_turns = randint(0, 1)
print('Решаем, кто будет ходить первым')
for i in range(randint(10, 20)):
    print(f'\033[01;{randint(30, 37)}m.\033[0m', end='')
    sleep(0.01 * i * 1.5)
print(' игрок!' if who_turns == 1 else ' бот')
while True:
    if who_turns:
        player_turn()
        bot_turn()
    else:
        bot_turn()
        player_turn()