def insertion_sort(a):

    for j in range(1, len(a)):
        # the array a[0:j] (i.e. j excluded, is sorted)
        swap_with = j
        while a[swap_with - 1] > a[swap_with] and swap_with > 0:
            swap(a, swap_with - 1, swap_with)
            swap_with -= 1


def swap(a, i, j):
    if i != j:
        tmp_a_i = a[i]
        a[i] = a[j]
        a[j] = tmp_a_i