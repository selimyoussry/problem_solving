def read():
    f = open('data.txt', 'r')

    matrix = []

    for l in f:
        matrix.append(
            map(
                lambda s: int(s),
                l.split(' ')
            )
        )
    return matrix

def get_combinations(m, p=4):
    all = combinations_down(m, p) +\
          combinations_right(m, p) +\
          combinations_diag_bottom(m, p) +\
          combinations_diag_top(m, p)
    return all

def combinations_down(m, p=4):
    dim = len(m)

    combinations = list()

    for i in range(dim - p + 1):
        for j in range(dim):
            product = 1
            for k in range(p):
                product *= m[i + k][j]

            combinations.append(
                product
            )

    return combinations

def combinations_right(m, p=4):
    dim = len(m)

    combinations = list()

    for j in range(dim - p + 1):
        for i in range(dim):
            product = 1
            for k in range(p):
                product *= m[i][j + k]

            combinations.append(
                product
            )

    return combinations

def combinations_diag_top(m, p=4):
    dim = len(m)

    combinations = list()

    for i in range(dim - p + 1):
        for j in range(dim - p + 1):
            product = 1
            for k in range(p):
                product *= m[i + k][j + k]

            combinations.append(
                product
            )

    return combinations

def combinations_diag_bottom(m, p=4):
    dim = len(m)

    combinations = list()

    for i in range(p - 1, dim):
        for j in range(dim - p + 1):
            product = 1
            for k in range(p):
                product *= m[i - k][j + k]

            combinations.append(
                product
            )

    return combinations


def solve():
    return max(
        get_combinations(
            read(),
            4
        )
    )