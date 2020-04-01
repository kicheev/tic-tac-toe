import random


def line_to_matrix(line, dimension=3):

    if len(line) < dimension ** 2:
        line = line + ' ' * (dimension ** 2 - len(line))

    matrix = [['' for j in range(dimension)] for i in range(dimension)]
    for i in range(dimension):
        for j in range(dimension):
            matrix[i][j] = line[j]
        line = line[dimension:]
    return matrix


def print_matrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()


def print_matrix_with_borders(matrix, dimension=3):

    ud_borders = '-'
    lr_borders = '|'

    border_lenght = dimension + 2

    print(ud_borders * (border_lenght * 2 - 1))
    for i in range(dimension):
        for j in range(border_lenght):
            if j == 0:
                print(lr_borders, end=' ')
            elif j == border_lenght - 1:
                print(lr_borders)
            else:
                print(matrix[i][j-1], end=' ')
    print(ud_borders * (border_lenght * 2 - 1))


def check_state(matrix):

    win_cases = []

    # Count marks
    Xs, Os, Ss = 0, 0, 0
    for i in matrix:
        for j in i:
            Xs += 1 if j == 'X' else 0
            Os += 1 if j == 'O' else 0
            Ss += 1 if j == ' ' else 0

    # Horizontals
    for i in matrix:
        win_cases.append(i)

    # Verticals
    for j in range(len(matrix)):
        win_cases.append([matrix[i][j] for i in range(len(matrix))])

    # Diagonals
    win_cases.append([matrix[i][i] for i in range(len(matrix))])
    win_cases.append([matrix[i][-(i+1)] for i in range(len(matrix))])

    # Win cases counter
    win_cases_counter = 0
    win_mark = ''
    for i in win_cases:
        if len(set(i)) == 1 and i[0] != ' ':
            win_cases_counter += 1
            win_mark = i[0]

    # Check state
    if abs(Xs - Os) > 1:
        print('Impossible')
    elif win_cases_counter > 1:
        print('Impossible')
    elif win_cases_counter == 1:
        print(win_mark, 'wins')
        return True
    elif Ss == 0:
        print('Draw')
        return True
    # else:
    #     print('Game not finished')

    return False


def input_coordinates(mark, dimension=3):

    global matrix

    while True:

        input_string = [i for i in input('Enter the coordinates: ').split()]

        if (len(input_string) < 2) or not (input_string[0].isdigit() and input_string[1].isdigit()):
            print('You should enter numbers!')
            continue

        x = int(input_string[0])
        y = int(input_string[1])

        if not ((1 <= x <= dimension) and (1 <= y <= dimension)):
            print('Coordinates should be from 1 to 3!')
            continue

        if matrix[-y][x-1] != ' ':
            print('This cell is occupied! Choose another one!')
            continue

        else:
            matrix[-y][x-1] = mark
            break


# list_of_states = ['XXXOO__O_', 'XOXOXOXXO', 'XOOOXOXXO', 'XOXOOXXXO', 'XO_OOX_X_', 'XO_XO_XOX', '_O_X__X_X', '_OOOO_X_X']
# matrix = line_to_matrix(list_of_states[5])
matrix = line_to_matrix('')
marks = (' ', 'X', 'O')
mark_index = 1

print_matrix_with_borders(matrix)

while not check_state(matrix):

    input_coordinates(marks[mark_index])
    mark_index = -mark_index

    print_matrix_with_borders(matrix)
