from random import choice 
from data import print_play, human_move, move_elements, check_win

first = input('Введите имя первого игрока: ')
second = input('Введите имя второго игрока: ')
first_player = choice([first,second])
second_player = second if first_player == first else first

print('\nИгра в крестики-нолики начинается с хода игрока,\n' 
        'который ставит крестик в свободное поле. Для этого укажите номер свободной ячейки\n')

elements = list(range(1,10))
game_over = False
flag = first_player
count = 0 
while game_over == False and count < 9:
    count+=1
    print_play(elements)
    if flag:
        move = human_move(first_player)
        char = 'x'
        elements = move_elements(elements, move, char)
        win = check_win(elements)
        if win != '':
            game_over = True    
        flag = False
    else:
        move = human_move(second_player)
        char = 'o'
        elements = move_elements(elements, move, char) 
        win = check_win(elements)  
        if win != '':
            game_over = True    
        flag = True

print_play(elements)

if win == 'x':
    print(f'\nВыйграл: {first_player}\n')
elif win == 'o':
    print(f'\nВыйграл: {second_player}\n')    
else:
    print('\n\nНичья - победителей НЕТ!!!\n')  