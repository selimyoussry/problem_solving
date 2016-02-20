# solution.py
import time


def msi(a):
    start_t = time.time()

    if len(a) == 1:
        return a, 0

    mid_point = len(a) // 2
    sorted_left, n_inversions_left = msi(a[:mid_point])
    sorted_right, n_inversions_right = msi(a[mid_point:])

    sorted_a, n_inversions = merge(sorted_left, sorted_right, n_inversions_left, n_inversions_right)

    return sorted_a, n_inversions

def msi_time_it(a):
    start_t = time.time()

    _, n_inversions = msi(a)

    return n_inversions, time.time() - start_t

def merge(a, b, n_inversions_left, n_inversions_right):
    """
    :param a: array
    :return:
    """
    i = 0
    j = 0
    k = 0
    total = len(a) + len(b)

    total_inversions = n_inversions_left + n_inversions_right

    out = []

    while k < total:

        if i == len(a):
            out.append(b[j])
            total_inversions += (len(a) - i)
            j += 1
        elif j == len(b):
            out.append(a[i])
            i += 1
        elif a[i] < b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            total_inversions += (len(a) - i)
            j += 1

        k += 1

    return out, total_inversions


def count_inversions_naive(a):
    start_t = time.time()

    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                count += 1

    return count, time.time() - start_t
