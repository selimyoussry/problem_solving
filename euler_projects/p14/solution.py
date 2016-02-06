def collatz(n, l):

    if n == 1:
        l.append(1)
        return l
    elif n % 2 == 0:
        new = n / 2
    else:
        new = 3 * n + 1

    l.append(new)
    return collatz(new, l)

def solve():

    maxi = 1 * 1000 * 1000
    winner = 1
    max_len = 1
    for n in range(1, maxi + 1):
        col = collatz(n, [])
        if len(col) > max_len:
            winner = n
            max_len = len(col)

        if n % 1000 == 0:
            print 'Done', n
    return winner
