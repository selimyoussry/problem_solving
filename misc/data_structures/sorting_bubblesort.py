
def swap(a, i, j):
    tmp_a_i = a[i]
    a[i] = a[j]
    a[j] = tmp_a_i

def bubble_sort(a):

    lo = 0
    hi = len(a) - 2
    n_swaps = 1

    while lo < hi and n_swaps > 0:
        n_swaps = 0

        for i in range(lo, hi + 1):
            if a[i] > a[i + 1]:
                swap(a, i, i+1)
                n_swaps += 1
        hi -= 1
