from random import choice
from data import total, one_move, human_takes_sweets, bot_takes_sweets

print('-----------------------------------------------------------------------')
print(f'\nВ игре {total} конфет и за один ход можно взять не более {one_move} штук\n')
print('-----------------------------------------------------------------------')

first = input('Введите имя игрока: ')
second = 'Bot'
first_player = choice([first,second])
second_player = second if first_player == first else first

while total > one_move:
    if first_player == first:
        sweets = human_takes_sweets(first) 
        total -= sweets 
        winner = second
        first_player = second

    else:
        sweets = bot_takes_sweets()
        total -= sweets 
        winner = first
        print(f'\nОсталось конфет: {total}\n')
        print('-------------------------------------------------------------')
        first_player = first

print(f'\nВыйграл: {winner}\n')