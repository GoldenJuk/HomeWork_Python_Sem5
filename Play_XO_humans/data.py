def print_play(element):
    print()
    print( 
    element[0], '|',
    element[1], '|',
    element[2])
    print('----------')
    print( 
    element[3], '|',
    element[4], '|',
    element[5])
    print('----------')
    print( 
    element[6], '|',
    element[7], '|',
    element[8])

def human_move(player):
    while True:
        try:
            print(f'\n{player},')
            move = int(input('сделай ход: '))
            if 0 < move <= 9:
                return move 
            else:
                print(f'Выбор должен быть от 1 до 9. Попробуйте еще раз.')    
        except:
            print(f'ОШИБКА!!! Должно быть число от 1 до 9')    

def move_elements(elements, move, char):
    indx = elements.index(move)
    elements[indx] = char
    return elements

def check_win(elements):
    winning = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    win = ''
    for i in winning:
        if elements[i[0]] == 'x' and elements[i[1]] == 'x' and elements[i[2]] == 'x': 
            win = 'x'
        if elements[i[0]] == 'o' and elements[i[1]] == 'o' and elements[i[2]] == 'o': 
            win = 'o'
    return win    

