import heapq

def heapsort(a):
    h = []
    for value in a:
        heapq.heappush(h, value)
    len_h = len(h)
    return [heapq.heappop(h) for i in range(len_h)]
