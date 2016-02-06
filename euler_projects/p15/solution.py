def npaths(i, j, m, total):
    if i == m or j == m:
        return m + 1
    else:
        return npaths(i + 1, j, m, total + 1) + npaths(i, j + 1, m, total + 1)

