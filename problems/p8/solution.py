import os

class Adjacent:

    def __init__(self):
        self.data_path = os.path.join(os.path.dirname(__file__), 'data.txt')
        self.data = self.read_data()

    def read_data(self):
        f = open(self.data_path, 'r')
        s = []
        for l in f:
            s.extend(map(lambda u: int(u), l.replace('\n', '').strip()))
        return s

    @staticmethod
    def mult(l):
        out = 1
        for e in l:
            out *= e
        return out

    def find_biggest_adjacent(self, size):
        m = []
        for i in range(len(self.data) - size + 1):
            slice_data = self.data[i:(i+size)]
            m.append(self.mult(slice_data))
        return max(m)
