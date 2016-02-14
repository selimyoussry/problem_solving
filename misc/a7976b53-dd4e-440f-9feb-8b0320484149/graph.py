
class Graph:

    def __init__(self):
        self.graph = dict()

    def find_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        elif start not in self.graph:
            return None

        for node in self.graph[start]:
            if node not in path:
                new_path = self.find_path(node, end, path)
                if new_path is not None:
                    return new_path

        return None

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph:
            return []
        paths = []
        for node in self.graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            return None
        shortest = None
        for node in self.graph[start]:
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
