from random import choice
from data import total, one_move, human_takes_sweets, bot_takes_sweets

print('-----------------------------------------------------------------------')
print(f'\nВ игре {total} конфет и за один ход можно взять не более {one_move} штук\n')
print('-----------------------------------------------------------------------')

first = input('Введите имя игрока: ')
second = 'Bot'
first_player = choice([first,second])
second_player = second if first_player == first else first

if first_player == second:
    while total > one_move:
        player = bot_takes_sweets(total)
        total -= player 
        winner = first
        if total > one_move:
            player = human_takes_sweets(first) 
            total -= player 
            winner = second
            print(f'\nОсталось конфет: {total}\n')
            print('-------------------------------------------------------------')
else:
    while total > one_move:
        player = human_takes_sweets(first)
        total -= player  
        winner = second
        if total > one_move:
            player = bot_takes_sweets(total)
            total -= player 
            print(f'\nОсталось конфет: {total}\n')
            print('-------------------------------------------------------------')
            winner = first

print(f'\nВыйграл: {winner}\n')