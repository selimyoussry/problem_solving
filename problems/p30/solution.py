def match_condition(x, n=5):
    """
    :type x: int
    :return:
    """
    digits = map(lambda u: int(u), str(x))
    return sum([pow(digit, n) for digit in digits]) == x

def solve(n, min_=2, max_=10*1000 * 1000):
    solutions = []
    for x in range(min_, max_):
        if match_condition(x, n):
            solutions.append(x)
    return solutions
