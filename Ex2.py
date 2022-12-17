#Создайте программу для игры с конфетами человек против человека.

#Условие задачи: На столе лежит 2021(или сколько вы скажете) конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28(или сколько вы зададите в начале) конфет. Все конфеты оппонента достаются сделавшему последний ход. Сделайте эту игру.
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""

from random import randint

# количество конфет
num_sweets = 2021
# можно взять конфет максимально:
max_sweets = 28


def player_take(num):  # проверка ввода игроком
    while True:
        try:
            num = int(num)
        except ValueError:
            num = input('Нужно ввести цифру. Попробуй сначала: ')
        else:
            if num > max_sweets or num < 1:
                num = input('Столько брать нельзя! Попробуй сначала: ')
            else:
                break
    return num


def lets_play_bot(cur_sweets_num):  # бот ходит первый
    if 0 < cur_sweets_num <= max_sweets:
        print(f'Выиграл бот, так как осталось {cur_sweets_num} конфет')
        return
    print(f'У нас есть {cur_sweets_num} конфет. Брать можно от 1 до 28 конфеты.')
    if cur_sweets_num <= max_sweets * 2:  # на последнем ходу у бота будет выбор: выиграть или выиграть
        player1 = cur_sweets_num - max_sweets - 1
    else:
        player1 = randint(1, max_sweets + 1)  # а это просто ходы
    print(f'Бот взял {player1} конфет.')
    if 0 < cur_sweets_num - player1 <= max_sweets:
        print(f'Выиграл игрок, так как осталось {cur_sweets_num - player1} конфет')
        return
    else:
        player2 = player_take(input('Ходи, игрок. Сколько берёшь? '))
    lets_play_bot(cur_sweets_num - (player1 + player2))


def lets_play_bot2(cur_sweets_num):  # бот ходит второй, так что выигрышную стратегию не применить
    if 0 < cur_sweets_num <= max_sweets:
        print(f'Выиграл игрок, так как осталось {cur_sweets_num} конфет')
        return
    print(f'У нас есть {cur_sweets_num} конфет. Брать можно от 1 до 28 конфеты.')
    player1 = player_take(input('Ходи, первый игрок. Сколько берёшь? '))
    if 0 < cur_sweets_num - player1 <= max_sweets:
        print(f'Выиграл бот, так как осталось {cur_sweets_num - player1} конфет')
        return
    else:
        if cur_sweets_num - player1 <= max_sweets * 3:  # надо продумать ходы заранее, чтоб на последнем был шанс
            if cur_sweets_num - player1 <= max_sweets * 2:  # а вот уже на последнем оставляем игроку max+1 конфет
                player2 = cur_sweets_num - player1 - max_sweets - 1
            else:
                player2 = cur_sweets_num - player1 - max_sweets * 2
        else:
            player2 = randint(1, max_sweets + 1)
    print(f'Бот взял {player2} конфет.')
    lets_play_bot2(cur_sweets_num - (player1 + player2))


def lets_play(cur_sweets_num):  # соревнование игроков
    if 0 < cur_sweets_num <= max_sweets:
        print(f'Выиграл первый, так как осталось {cur_sweets_num} конфет')
        return
    print(f'У нас есть {cur_sweets_num} конфет. Брать можно от 1 до 28 конфеты.')
    player1 = player_take(input('Ходи, первый игрок. Сколько берёшь? '))
    cur_sweets_num -= player1
    if 0 < cur_sweets_num <= max_sweets:
        print(f'Выиграл второй, так как осталось {cur_sweets_num} конфет')
        return
    else:
        player2 = player_take(input('Ходи, второй игрок. Сколько берёшь? '))
    lets_play(cur_sweets_num=cur_sweets_num - player2)


lets_play_bot(num_sweets)