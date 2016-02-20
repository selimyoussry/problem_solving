__author__ = 'somedude'

class DirectedWeightedGraph:

    def __init__(self, al, n, w=dict()):
        """
        :param al: adjacency list with costs
        :param n: number of vertices
        :param w: weights of the vertices (red lights)
        :return:
        """
        self.al = al
        self.n = n
        self.w = w if len(w) else dict([(v, 0) for v in self.al])

    def dijkstra(self, s):

        distances = dict([(v, 0) for v in self.al])
        explored = set(s)
        paths = dict([(v, []) for v in self.al])

        while len(explored) < self.n:

            min_crossing_edge = []
            min_cost = 1e9
            for u in explored:
                for v, weight in self.al[u]:
                    if v not in explored:
                        cost = weight + distances[u] + self.w[u]
                        if cost < min_cost:
                            min_crossing_edge = (u, v)
                            min_cost = cost
            u, v = min_crossing_edge
            paths[v] = paths[u] + [v]
            distances[v] = min_cost
            explored.add(v)
            print explored

        return distances, explored, paths
