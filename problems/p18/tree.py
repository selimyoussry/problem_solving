class Triangle:

    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        f = open('data.txt', 'r')

        previous_layer = []
        current_layer = []
        for l in reversed([l for l in f]):
            nodes_values = map(lambda s: int(s), l.split(' '))
            n_nodes = len(nodes_values)

            if len(previous_layer) == 0:
                previous_layer = [Leaf(node_value) for node_value in nodes_values]
            else:
                current_layer = []
                for i in range(n_nodes):
                    current_layer.append(
                        BinaryTree(
                            nodes_values[i],
                            previous_layer[i],
                            previous_layer[i + 1]
                        )
                    )

                previous_layer = current_layer

        print 'current layer size', len(current_layer)

        return current_layer[0]


class BinaryTree:
    def __init__(self, n, left=None, right=None):
        """
        :type n: n
        :type left: BinaryTree
        :type right: BinaryTree
        """
        self.n = n
        self.left = left
        self.right = right

    def set_n(self, n):
        self.n = n

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def __repr__(self):
        return '{} \n{} \t {}\nBigTree'.format(self.n, self.left.n, self.right.n)


class Leaf(BinaryTree):
    def __repr__(self):
        return str(self.n)
