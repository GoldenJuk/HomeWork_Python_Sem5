from random import randint

total = 121
one_move = 28

def human_takes_sweets(player):
    while True:
        try:
            print(f'\n{player},')
            sweets = int(input('возьми конфеты: '))
            if 0 < sweets <= one_move:
                return sweets 
            else:
                print(f'Количество должно быть от 1 до {one_move} штук. Попробуйте еще раз.')    
        except:
            print(f'ОШИБКА!!! Должно быть число от 1 до {one_move} штук')

def bot_takes_sweets():
    sweets = randint(1, one_move)
    print(f'\nБот взял: {sweets} конфет')
    return sweets
