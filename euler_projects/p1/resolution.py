__author__ = 'somedude'

def multiples_of(n, lim):
    """
    :type n: int
    :type lim: int
    :return:
    """
    return [x * n for x in range(1, lim / n + 1)]

def multiples_of_several(n_list, lim):
    """
    :type n_list: list
    :type lim: int
    :return:
    """
    out = []
    for n in n_list:
        out.extend(
            multiples_of(n, lim)
        )
    return set(out)
