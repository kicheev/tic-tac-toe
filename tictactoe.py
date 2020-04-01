import random


def random_fill():
    n = 9
    set_cells = [i for i in range(n)]
    line_fill = ['O' for i in range(n)]

    for i in range(n // 2):
        rand = random.choice(set_cells)
        line_fill[rand] = 'X'
        set_cells.remove(rand)

    return line_to_matrix(line_fill)


def line_to_matrix(line):

    if len(line) < 9:
        line = line + ' ' * (9 - len(line))

    matrix_dim = 3
    matrix = [['' for j in range(matrix_dim)] for i in range(matrix_dim)]
    for i in range(matrix_dim):
        for j in range(matrix_dim):
            matrix[i][j] = line[j]
        line = line[matrix_dim:]
    return matrix


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()


def matrix_to_line(matrix):
    line = [j for i in matrix for j in i]
    return line


def add_borders(matrix):
    ud_borders = '-'
    lr_borders = '|'

    field_height = 5
    field_lenght = 9
    field = [[' ' for j in range(field_lenght)] for i in range(field_height)]

    line = matrix_to_line(matrix)
    line_index = 0

    for i in range(field_height):
        for j in range(field_lenght):
            if i == 0 or i == field_height - 1:
                field[i][j] = ud_borders
            elif j == 0 or j == field_lenght - 1:
                field[i][j] = lr_borders
            elif j % 2 == 0:
                field[i][j] = line[line_index]
                line_index += 1

    return field


def check_state(line):
    Xs = line.count('X')
    Os = line.count('O')
    Ss = line.count('_')

    win_cases = []

    for i in range(3):
        temp_list = []
        for j in range(i, i + 7, 3):
            temp_list.append(line[j])
        win_cases.append(''.join(temp_list))

    for i in range(0, 9, 3):
        win_cases.append(line[i:i + 3])

    temp_list = []
    for i in range(0, 9, 4):
        temp_list.append(line[i])
    win_cases.append(''.join(temp_list))

    temp_list = []
    for i in range(2, 7, 2):
        temp_list.append(line[i])
    win_cases.append(''.join(temp_list))

    win_cases_counter = 0
    win_mark = ''

    for i in range(8):
        if len(set(win_cases[i])) == 1:
            win_cases_counter += 1
            win_mark = win_cases[i][0]

    if abs(Xs - Os) > 1:
        print('Impossible')
    elif win_cases_counter > 1:
        print('Impossible')
    elif win_cases_counter == 1:
        print(win_mark, 'wins')
    elif Ss == 0:
        print('Draw')
    else:
        print('Game not finished')

    return


def input_coordinates():

    global matrix

    while True:

        input_string = [i for i in input('Enter the coordinates: ').split()]

        if (len(input_string) < 2) or not (input_string[0].isdigit() and input_string[1].isdigit()):
            print('You should enter numbers!')
            continue

        x = int(input_string[0])
        y = int(input_string[1])

        if not ((1 <= x <= 3) and (1 <= y <= 3)):
            print('Coordinates should be from 1 to 3!')
            continue

        if matrix[-y][x-1] != ' ':
            print('This cell is occupied! Choose another one!')
            print(matrix[-y][x-1])
            continue

        else:
            matrix[-y][x-1] = 'X'
            break


input_list = ['X_X_O____', '_XXOO_OX_', '789456123']

input_string = input('Enter cells: ').replace('_', ' ')
# input_string = input_list[1].replace('_', ' ')

matrix = line_to_matrix(input_string)

field = add_borders(matrix)
for i in field:
    print(*i, sep='')

input_coordinates()

field = add_borders(matrix)
for i in field:
    print(*i, sep='')

# check_state(input_string)


