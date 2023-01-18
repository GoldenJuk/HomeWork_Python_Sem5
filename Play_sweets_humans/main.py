from random import choice
from data import total, one_move, take_sweets

print('-----------------------------------------------------------------------')
print(f'\nВ игре {total} конфет и за один ход можно взять не более {one_move} штук\n')
print('-----------------------------------------------------------------------')

first = input('Введите имя первого игрока: ')
second = input('Введите имя второго игрока: ')
first_player = choice([first,second])
second_player = second if first_player == first else first

while total > one_move:
    sweets = take_sweets(first_player) 
    total -= sweets 
    winner = second_player

    if total > one_move:
        sweets = take_sweets(second_player)
        total -= sweets 
        print(f'\nВСЕГО конфет: {total}\n')
        print('-------------------------------------------------------------')
        winner = first_player
        
print('-----------------------------------------------------------------------')
print(f'\nВыйграл: {winner}\n')