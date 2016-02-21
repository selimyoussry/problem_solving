"""
We basically want to implement Dijkstra's algorithm
but change the addition to bitwise OR
"""
import sys


class UndirectedGraph:
    def __init__(self, uvc, n, m):
        self.n = n
        self.m = m
        self.al = self.create_al(uvc)

    @staticmethod
    def create_al(uvc):
        al = dict()
        for u, v, c in uvc:
            if u in al:
                al[u].add((v, c))
            else:
                al[u] = {(v, c)}

            if v in al:
                al[v].add((u, c))
            else:
                al[v] = {(u, c)}
        return al

    def dijkstra(self, s):
        distances = dict([(node, 0) for node in self.al])
        explored = {s}

        while len(explored) < self.n:

            min_distance = 1e9
            min_crossing_edge = (-1, -1, 0)
            v, c = -1, 0
            for u in explored:
                for v, c in [(v_, c_) for (v_, c_) in self.al[u] if v_ not in explored]:
                    distance = distances[u] | c
                    if distance < min_distance:
                        min_crossing_edge = (u, v, c)
                        min_distance = distance
            u, v, c = min_crossing_edge
            distances[v] = min_distance
            explored.add(v)

        return distances

def reader():
    uvc = []
    n, m, s, e = 0, 0, 0, 0
    counter = 0
    for l in sys.stdin:

        if counter == 0:
            n, m = map(int, l.split(' '))

        if 0 < counter <= m:
            uvc.append(
                map(int, l.split(' '))
            )

        if counter == m + 1:
            s, e = map(int, l.split(' '))

        counter += 1

    return uvc, n, m, s, e


if __name__ == '__main__':
    uvc, n, m, s, e = reader()
    ug = UndirectedGraph(uvc, n, m)
    distances = ug.dijkstra(s)
    print distances[e]
