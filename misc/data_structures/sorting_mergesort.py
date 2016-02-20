def merge_sort(a):

    if len(a) == 1:
        return a

    mid = len(a) // 2

    x = merge_sort(a[:mid])
    y = merge_sort(a[mid:])

    return merge(x, y)

def merge(x, y):
    """
    :param x: sorted array
    :param y: sorted array
    :return:
    """
    i = 0
    j = 0
    k = 0
    ret = []
    total_size = len(x) + len(y)
    len_x = len(x)
    len_y = len(y)

    while k < total_size:
        if i<len_x and j<len_y:
            if x[i] < y[j]:
                ret.append(x[i])
                i += 1
            else:
                ret.append(y[j])
                j += 1
        elif i == len_x:
            ret.append(y[j])
            j += 1
        else:
            ret.append(x[i])
            i += 1
        k += 1

    return ret
