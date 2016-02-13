# solution.py

# This would have a worst case complexity n log(k)

def insertion_sort_solution(a, k):
    for j in range(1, len(a)):
        i = j - 1
        n_swaps = 0
        while i >= 0 and a[i + 1] < a[i] and n_swaps <= k:
            swap(a, i, i+1)
            i -= 1
            n_swaps += 1

def swap(a, i, j):
    tmp_a_i = a[i]
    a[i] = a[j]
    a[j] = tmp_a_i
