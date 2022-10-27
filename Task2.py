# Создайте программу для игры с конфетами человек против человека.
#
from random import randint

def humans (candies, max_candies):   # (конфеты, макс кол конфет за ход)
    player = 0                  # номер игрока - инициализация переменной
    player_1 = input('Введите имя первого игрока: ')
    player_2 = input('Введите имя второго игрока: ')

    first_move = randint(1, 2)  # Случайный выбор игрока для первого хода 
    while candies > 0:
        if first_move == 1:     # Выбран первый игрок
            player = 1          # Выбран первый игрок
            move = int(input(f'{player_1} возьмите не больше {max_candies} конфет: '))  
            while move < 0 or move > max_candies or move > candies: # Проверка кол-ва взятых конфет
                move = int(input(f'{player_1} возьмите не больше {max_candies} конфет: '))
            candies -= move     # Определяем остаток конфет после 1-го игрока
            print(f'Осталось {candies} конфет.')
            if candies == 0:
                break           # Если конфет не осталось выходим из цикла
                
            player = 2          # Ход второго игрока
            move = int(input(f'{player_2} возьмите не больше {max_candies} конфет: '))
            while move < 0 or move > max_candies or move > candies:      # Проверка кол-ва взятых конфет
                move = int(input(f'{player_2} возьмите не больше {max_candies} конфет: '))
            candies -= move     # Определяем остаток конфет после 2-го игрока
            print(f'Осталось {candies} конфет.')
            if candies == 0:
                break           # Если конфет не осталось выходим из цикла
        else:                   # Выбран второй игрок
            player = 2          # Выбран второй игрок
            move = int(input(f'{player_2} возьмите не больше {max_candies} конфет: '))
            while move < 0 or move > max_candies or move > candies:      # Проверка кол-ва взятых конфет
                move = int(input(f'{player_2} возьмите не больше {max_candies} конфет: '))
            candies -= move     # Определяем остаток конфет после 2-го игрока
            print(f'Осталось {candies} конфет.')
            if candies == 0:
                break           # Если конфет не осталось выходим из цикла

            player = 1          # Ход первого игрока
            move = int(input(f'{player_1} возьмите не больше {max_candies} конфет: '))
            while move < 0 or move > max_candies or move > candies:      # Проверка кол-ва взятых конфет
                move = int(input(f'{player_1} возьмите не больше {max_candies} конфет: '))
            candies -= move     # Определяем остаток конфет после 1-го игрока
            print(f'Осталось {candies} конфет.')
            if candies == 0:
                break           # Если конфет не осталось выходим из цикла
    winner = player_1 if player == 1 else player_2
    print(f'Победил игрок {winner}')

def human_bot (candies, max_candies, iq):
    player = 0                  # Инициализация переменной
    player_human = input('Введите свое имя: ')
    first_move = randint(1, 2)
    while candies > 0:
        if first_move == 1:     # Выбран человек
            player = 1          # Ход человека
            print(f'Ход игрока {player_human}.')
            move = int(input(f'{player_human} возьмите не больше {max_candies} конфет: '))
            while move < 0 or move > max_candies or move > candies:      # Проверка кол-ва взятых конфет
                move = int(input(f'{player_human} возьмите не больше {max_candies} конфет: '))
            candies -= move             # Определяем остаток конфет после человека
            print(f'Осталось {candies} конфет.')
            if candies == 0:            # Если конфет не осталось выходим из цикла
                break
            
            player = 2                  # Ход компьютера
            if candies <= max_candies:  # Если конфет осталось меньше 28
                move = candies          #То компьтер берет весь остаток
            else:
                if iq == 1:             # Если компьютер глупый, то он возьмет
                    move = randint(1, max_candies) # слуйное кол-во конфет до 28 
                elif iq == 0:           # Если не глупый, то возьмет по формуле
                    move = candies - max_candies * (candies // max_candies) - 1
                    if move <= 0:
                        move += max_candies
            print(f'Компьютер забрал {move} конфет.')
            candies -= move            # Определяем остаток конфет после человека
            print(f'Осталось {candies} конфет.')
            if candies == 0:
                break           # Если конфет не осталось выходим из цикла
        else:
            player == 2                 # Ход компьютера
            if candies <= max_candies:  # Если конфет осталось меньше 28
                move = candies          #То компьютер берет весь остаток
            else:
                if iq == 1:            # Если компьютер глупый, то он возьмет
                    move = randint(1, max_candies)  # слуйное кол-во конфет до 28
                elif iq == 0:          # Если не глупый, то возьмет по формуле
                    move = candies - max_candies * (candies // max_candies) - 1
                    if move <= 0:
                        move += max_candies
            print(f'Компьютер забрал {move} конфет.')
            candies -= move            # Определяем остаток конфет после компьютера
            print(f'Осталось {candies} конфет.')
            if candies == 0:           # Если конфет не осталось выходим из цикла
                break
            player = 1
            print(f'Ход игрока {player_human}.')
            move = int(input('Введите количество конфет, которые Вы заберете: '))
            candies -= move
            print(f'Осталось {candies} конфет.')
            if candies == 0:
                break           # Если конфет не осталось выходим из цикла
    if player == 1:
        winner = player_human
    else:
        winner = 'компьютер'
    print(f'Победитель - {winner}')

all_candies = 121      # Общее кол-во конфет
max_pieces = 28       # Макс-ое кол-во конфет за один ход
print('1 - играть вдвоем')
print('2 - играть с компьютером')
print('3 - играть с "умным" компьютером')
game_level = int(input('Введите с кем хотите играть: '))
if(game_level == 1):
    humans (all_candies, max_pieces)
elif (game_level == 2):
    human_bot(all_candies, max_pieces, 0)
elif (game_level == 3):
    human_bot(all_candies, max_pieces, 1)