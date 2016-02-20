from collections import deque


class DirectedGraph:

    def __init__(self, al, n):
        """
        :param al: adjacency list
        :return:
        """

        self.al = al
        self.n = n

    def bfs(self, s):
        """
        :param s: start node
        :return:
        """
        explored = {s}

        distances = dict([(node, self.n + 1) for node in self.al])
        distances[s] = 0

        parents = dict([(node, 0) for node in self.al])

        unexplored_nodes = self.al[s]
        q = deque(unexplored_nodes)
        for node in unexplored_nodes:
            explored.add(node)
            for node in unexplored_nodes:
                distances[node] = distances[s] + 1
                parents[node] = s
                explored.add(node)

        while len(q) > 0:

            c_node = q.popleft()

            unexplored_nodes = [neighbor for neighbor in self.al[c_node] if neighbor not in explored]
            q.extend(
                unexplored_nodes
            )
            for node in unexplored_nodes:
                distances[node] = distances[c_node] + 1
                parents[node] = c_node
                explored.add(node)

        return distances, parents, explored

    def dfs(self):
        """
        :return:
        """
        explored = set()
        nodes_label = dict([(node, -1) for node in self.al])
        current_label = [self.n]

        def dfs_rec(s):
            unexplored_neighbors = deque([v for v in self.al[s] if v not in explored]) if s in self.al else deque()

            print 'Starting dfs_rec with {}, discovered so far {} - {}'.format(s, explored, unexplored_neighbors)

            for v in unexplored_neighbors:
                explored.add(v)
            while len(unexplored_neighbors) > 0:
                start_node = unexplored_neighbors.popleft()
                dfs_rec(start_node)

            print 'Assigning label {} to {}'.format(current_label[0], s)
            nodes_label[s] = current_label[0]
            current_label[0] -= 1

        for vertex in self.al:
            if vertex not in explored:
                dfs_rec(vertex)

        return nodes_label
