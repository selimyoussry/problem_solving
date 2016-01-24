# Square difference
# Just need to compute the cross product of distinct numbers and double it

def diff(n):
    cumsum = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            cumsum += (2 * i * j)
    return cumsum
