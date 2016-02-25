__author__ = 'somedude'
"""
This algorithm is in place
"""

def quicksort(a):
    return quicksort_(a, 0, len(a) - 1)


def quicksort_(a, lo, hi):

    if lo < hi:
        p = partition(a, lo, hi)
        # All the numbers before the index p, are lower than a[p]
        # after p, they are greater than a[p]
        quicksort_(a, lo, p-1)
        quicksort_(a, p+1, hi)


def partition(a, lo, hi):
    # returns an index of an element that is at the correct position
    # everything on the right is greater
    # everything on the left is lower
    pivot = a[hi]

    p = lo
    for j in range(lo, hi):
        if a[j] <= pivot:
            swap(a, j, p)
            p += 1
    swap(a, p, hi)
    return p

def swap(a, i, j):
    tmp_a_i = a[i]
    a[i] = a[j]
    a[j] = tmp_a_i
