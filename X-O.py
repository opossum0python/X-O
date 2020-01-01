print('Игра "Крестики-нолики"!')

def game():
    print('Игрок 1 == O')
    print('Игрок 2 == X\n')
    lines = '1 2 3\n4 5 6\n7 8 9\n'
    iters = 0
    print(lines)
    eror = 'Ход невозможен, попробуйте еще раз!'
    while True:
        if iters == 8:
            print('Ничья!')
            break
        print('Ход игрока под номером {}'.format((iters%2)+1))
        x = input('введите номер оконки(1-9)')
        print()
        c = True
        for i in '123456789':
            if x == i:
                c = False
        if c:
            print('Неверно введено значение')
            continue

        x = int(x)

        if iters % 2 == 0:
            z = 'O'
        else:
            z = 'X'

        if x == 1:
            if lines[0] == 'X' or lines[0] == 'O':
                print(eror)
                continue
            lines = lines.replace(lines[0], z)

        elif x == 2:
            if lines[2] == 'X' or lines[2] == 'O':
                print(eror)
                continue
            lines = lines.replace(lines[2], z)

        elif x == 3:
            if lines[4] == 'X' or lines[4] == 'O':
                print(eror)
                continue
            lines = lines.replace(lines[4], z)

        elif x == 4:
            if lines[6] == 'X' or lines[6] == 'O':
                print(eror)
                continue
            lines = lines.replace(lines[6], z)

        elif x == 5:
            if lines[8] == 'X' or lines[8] == 'O':
                print(eror)
                continue
            lines = lines.replace(lines[8], z)

        elif x == 6:
            if lines[10] == 'X' or lines[10] == 'O':
                print(eror)
                continue
            lines = lines.replace(lines[10], z)

        elif x == 7:
            if lines[12] == 'X' or lines[12] == 'O':
                print(eror)
                continue
            lines = lines.replace(lines[12], z)

        elif x == 8:
            if lines[14] == 'X' or lines[14] == 'O':
                print(eror)
                continue
            lines = lines.replace(lines[14], z)

        elif x == 9:
            if lines[16] == 'X' or lines[16] == 'O':
                print(eror)
                continue
            lines = lines.replace(lines[16], z)
        else:
            continue

        if lines[0] == lines[2] == lines[4]:
            print(lines)
            print('Game Over')
            print('Победил игрок под номером {}'.format((iters%2)+1))
            break
        elif lines[6] == lines[8] == lines[10]:
            print(lines)
            print('Game Over')
            print('Победил игрок под номером {}'.format((iters%2)+1))
            break
        elif lines[12] == lines[14] == lines[16]:
            print(lines)
            print('Game Over')
            print('Победил игрок под номером {}'.format((iters%2)+1))
            break
        elif lines[0] == lines[6] == lines[12]:
            print(lines)
            print('Game Over')
            print('Победил игрок под номером {}'.format((iters%2)+1))
            break
        elif lines[2] == lines[8] == lines[14]:
            print(lines)
            print('Game Over')
            print('Победил игрок под номером {}'.format((iters%2)+1))
            break
        elif lines[4] == lines[10] == lines[16]:
            print(lines)
            print('Game Over')
            print('Победил игрок под номером {}'.format((iters%2)+1))
            break
        elif lines[0] == lines[8] == lines[16]:
            print(lines)
            print('Game Over')
            print('Победил игрок под номером {}'.format((iters%2)+1))
            break
        elif lines[4] == lines[8] == lines[12]:
            print(lines)
            print('Game Over')
            print('Победил игрок под номером {}'.format((iters%2)+1))
            break
        iters +=1
        print(lines)
while True:
    game()
    x = input('Если не хотите больше играть введите "1"')
    if x == 1:
        break
print('Спасобо за игру')
