def find_cap(g, b):
    n = len(b)

    s_b = sorted(g)

    total = sum(g)
    
    if total <= b:
        return s_b[-1]

    partial_sums = [s_b[0]] * n
    for i in range(1, n):
        partial_sums[i] = s_b[i] + partial_sums[i - 1]

    i = n - 1
    while total > b and i >= 0:
        c = s_b[i]
        total = c * (n - i) + (partial_sums[i - 1] if i >= 1 else 0)
        i -= 1

    if total == b:
        return c

    if i == 0:
        return float(b) / n

    return (float(b) - partial_sums[i]) / (n - 1)
