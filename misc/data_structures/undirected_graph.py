from collections import deque


class UndirectedGraph:

    def __init__(self, al):
        """
        :param al: adjacency list (dict of vertex: set(edges))
        :return:
        """
        self.al = al
        self.n = len(self.al)

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

    def dfs(self, s):
        """
        :param s: start node
        :return:
        """

        explored = {s}

        def dfs_rec(s):
            unexplored_neighbors = deque([node for node in self.al[s] if node not in explored])

            print 'Starting dfs_rec with {}, discovered so far {} - {}'.format(s, explored, unexplored_neighbors)

            for node in unexplored_neighbors:
                explored.add(node)
            while len(unexplored_neighbors) > 0:
                start_node = unexplored_neighbors.popleft()
                dfs_rec(start_node)
        dfs_rec(s)

    def connected_components(self):
        components = dict([(node, -1) for node in self.al])
        current_component = 0

        explored = set()

        for node in self.al:
            if node not in explored:
                _, _, this_explored = self.bfs(node)
                for elt in this_explored:
                    explored.add(elt)
                    components[elt] = current_component
                current_component += 1

        return components
