# размерность
DIM = 3


def generate_grid():
    grid = [[0 for j in range(DIM)] for i in range(DIM)]
    return grid


def render_grid(M):
    # clear screen
    print('\n' * 100)
    # header
    print('  ', end='')
    for i in range(0, DIM):
        print(str(i) + ' ', end='')
    print('')
    # body
    for i in range(0, len(M)):
        print(str(i) + ' ', end='')
        for j in range(0, len(M[i])):
            if M[i][j] == 0:
                character = '-'
            else:
                character = M[i][j]
            print(str(character) + ' ', end='')
        print('')


def check_winner(M):
    # check row
    for i in range(0, len(M)):
        if M[i].count(M[i][0]) == DIM and M[i][0] != 0:
            winner = M[i][0]
            return winner

    # check col
    for column in zip(*M):
        if column.count(column[0]) == DIM and column[0] != 0:
            winner = column[0]
            return winner

    # check diag1
    diag = []
    j = 0
    for i in range(0, len(M)):
        if j < DIM:
            diag.append(M[i][j])
            j = j + 1
    if diag.count(diag[0]) == DIM and diag[0] != 0:
        winner = diag[0]
        return winner

    # check diag2
    diag = []
    j = DIM - 1
    for i in range(0, len(M)):
        if j >= 0:
            diag.append(M[i][j])
            j = j - 1
    if diag.count(diag[0]) == DIM and diag[0] != 0:
        winner = diag[0]
        return winner
    return 0


def the_game():
    M = generate_grid()

    turn_count = 1
    while any(0 in sublist for sublist in M):
        render_grid(M)
        cmd_valid = False
        if turn_count % 2:
            current_player = 'x'
        else:
            current_player = 'o'
        while not cmd_valid:

            print("Ходит игрок " + current_player.capitalize())
            cmd = input('Введите две координаты через запятую: x,y ')
            if cmd.count(',') != 1: continue
            cmd = cmd.replace(' ', '')
            if not cmd.replace(',', '').isnumeric(): continue
            cmd_y, cmd_x = map(int, cmd.split(','))
            if DIM > cmd_x >= 0 and DIM > cmd_y >= 0:
                if M[cmd_x][cmd_y] == 0:
                    cmd_valid = True
                else:
                    print('Выберите незанятую позицию!')
            else:
                print('Координаты вне диапазона!')
        M[cmd_x][cmd_y] = current_player
        turn_count = turn_count + 1

        winner = check_winner(M)

        if winner:
            game_over(M, winner)
            return

    game_over(M, False)
    return


def game_over(M, winner):
    render_grid(M)
    if winner:
        print("Игра окончена! Победил игрок " + winner.capitalize())
    else:
        print("Игра окончена! Ничья!")


the_game()
