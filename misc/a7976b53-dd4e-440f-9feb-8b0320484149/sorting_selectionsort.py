
def selection_sort(a):

    lo = 0

    while lo < len(a) - 1:
        curr_min_idx = lo
        curr_min = a[curr_min_idx]
        idx = lo + 1
        for elt in a[(lo + 1):]:
            if elt < curr_min:
                curr_min_idx = idx
                curr_min = elt
            idx += 1
        swap(a, curr_min_idx, lo)
        lo += 1


def swap(a, i, j):
    if i == j:
        return True
    tmp_a_i = a[i]
    a[i] = a[j]
    a[j] = tmp_a_i
