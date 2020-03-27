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


test_str = 'O_OXXO_XX'
marks = ('X', 'O')

matrix = line_to_matrix(input('Enter cells: '))
# matrix = line_to_matrix(test_str)
field = add_borders(matrix)

for i in range(len(field)):
    print(*field[i], sep='')
