# solution.py

my_sum = 200
coins = [200, 100, 50, 20, 10, 5, 2, 1]



class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, obj):
        self.children.append(obj)


class Solver:

    def __init__(self):
        self.t = Node(
            data=(0, 0, 0)
        )
        self.t.add_child(
            Node((200, 0, 0, 0, [(200, 0)]))
        )

        self.t.add_child(
            Node((200, 1, 200, 0, [(200, 1)]))
        )
        self.n_solutions = 0

        self.paths = []

    def solve_rec(self, t):
        for child in t.children:
            coin_value, a, cum_sum, index, path = child.data
            if cum_sum == my_sum:
                self.paths.append(path)
                self.n_solutions += 1
            elif coin_value == 2:  # i.e. coin_value == 1
                new_path = path + [(1, my_sum - cum_sum)]
                self.paths.append(new_path)
                self.n_solutions += 1
            else:
                new_index = index + 1
                new_coin_value = coins[new_index]
                new_a = 0
                new_cum_sum = new_a * new_coin_value + cum_sum
                new_path = path + [(new_coin_value, new_a)]
                new_tree = Node(())
                while new_cum_sum <= my_sum:
                    new_tree.add_child(
                        Node(
                            (new_coin_value, new_a, new_cum_sum, new_index, new_path)
                        )
                    )
                    new_a += 1
                    new_cum_sum = new_a * new_coin_value + cum_sum
                    new_path = path + [(new_coin_value, new_a)]
                self.solve_rec(new_tree)

    def solve(self):
        self.solve_rec(self.t)

    def nested_loops(self):
        n = 0
        for a in range(my_sum, -1, -200):
            for b in range(a, -1, -100):
                for c in range(b, -1, -50):
                    for d in range(c, -1, -20):
                        for e in range(d, -1, -10):
                            for f in range(e, -1, -5):
                                for g in range(f, -1, -2):
                                    n += 1
        return n
