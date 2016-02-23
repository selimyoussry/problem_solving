import heapq


class SortingMethods:
    def __init__(self):
        pass

    @staticmethod
    def insertion_sort(a):
        for i in range(1, len(a)):
            j = i - 1
            while j >= 0 and a[j + 1] < a[j]:
                swap(a, j, j+1)
                j -= 1

    @staticmethod
    def swap(a, i, j):
        a_i = a[i]
        a[i] = a[j]
        a[j] = a_i

    @staticmethod
    def heap_sort(a):
        out = []
        heapq.heapify(a)
        for i in range(len(a)):
            out.append(heapq.heappop(a))

        return out

    @staticmethod
    def k_optimal_heap_sort(a, k):
        out = []

        sliding_window = heapq.heapify(
            a[:(k + 1)]
        )

        for elt in a[(k+1):]:
            out.append(
                heapq.heappop(sliding_window)
            )
            heapq.heappush(sliding_window, elt)

        while len(sliding_window) > 0:
            out.append(
                heapq.heappop(sliding_window)
            )

        return out
