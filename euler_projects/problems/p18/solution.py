class ArrayTriangle:

    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        f = open('data.txt', 'r')
        data = []
        for l in f:
            data.append(
                map(lambda s: int(s), l.split(' '))
            )
        return data

    def solve(self):
        size = len(self.data)

        for i in range(size - 2, -1, -1):

            for j in range(len(self.data[i])):
                self.data[i][j] += max(
                    self.data[i + 1][j],
                    self.data[i + 1][j + 1]
                )
        return self.data[0][0]
