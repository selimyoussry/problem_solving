class Triangle:

    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        f = open('data.txt', 'r')

        tree = TreeNode(0)

        for l in f:
            nodes = map(lambda s: int(s), l.split(''))
            for n in nodes:
                raise NotImplementedError


class TreeNode:
    def __init__(self, n, left=None, right=None):
        """
        :type n: n
        :type left: TreeNode
        :type right: TreeNode
        """
        self.n = n
        self.left = left
        self.right = right
