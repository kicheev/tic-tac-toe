import random


def random_fill():
    n = 9
    set_cells = [i for i in range(n)]
    line_fill = ['O' for i in range(n)]

    for i in range(n // 2):
        rand = random.choice(set_cells)
        line_fill[rand] = 'X'
        set_cells.remove(rand)

    fill_field = []
    while line_fill:
        fill_field.append(line_fill[:3])
        line_fill = line_fill[3:]

    return fill_field


marks = ('X', 'O')
dim = 3
field = [[0 for j in range(dim)]for i in range(dim)]

field = random_fill()

for i in range(dim):
    for j in range(dim):
        print(field[i][j], end=' ')
    print()
