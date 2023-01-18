total = 121
one_move = 28

def take_sweets(player):
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