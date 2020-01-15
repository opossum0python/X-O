print('Игра "Крестики-нолики"!')

def cheak_win(combinations):
    for i in combinations:
        x = []
        for j in i:
            x.append(j)
        if x[0] == x[1] == x[2]:
            return True
    return False

def change_lines(move, lines, iters):
    z = int(move) * 2 - 2
    if iters % 2 == 0:
        lines = lines.replace(lines[z], 'O')
    else:
        lines = lines.replace(lines[z], 'X')
    return lines

def game():
    print('Игрок 1 == O')
    print('Игрок 2 == X\n')
    iters = 0
    lines = '1 2 3\n4 5 6\n7 8 9\n'
    move_cheak = ''
    print(lines)
    while True:
        combinations = ((lines[0], lines[2], lines[4]), (lines[6], lines[8], lines[10]), (lines[12], lines[14], lines[16]), (lines[0], lines[8], lines[16]), (lines[4], lines[8], lines[12]), (lines[0], lines[6], lines[12]), (lines[2], lines[8], lines[14]), (lines[4], lines[10], lines[16]))
        
        if cheak_win(combinations):
            print(lines)
            print('Game Over')
            print('Победил игрок под номером {}'.format((iters%2)+1))
            break

        if iters == 9:
            print('Ничья!')
            break

        print('Ход игрока под номером {}'.format((iters%2)+1))

        move = input('введите номер оконки(1-9): ')
        cheak = True
        for i in '123456789':
            if move == i:
                cheak = False

        if cheak:
            print('Неверно введено значение')
            continue

        for i in move_cheak:
            if i == move:
                print('Ход невозможен, попробуйте еще раз!')
                cheak = True
                
        if cheak:
            continue

        move_cheak += move
        move = int(move)
        lines = change_lines(move, lines, iters)

        iters +=1
        print('\n', lines, sep = '')


while True:
    game()
    x = input('Если не хотите больше играть введите "1": ')
    if x == '1':
        break
	
print('Спасобо за игру')