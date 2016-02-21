import sys


class BeautifulString:

    def __init__(self, s):
        self.s = s
        self.n = len(self.s)

    @staticmethod
    def remove(s, i, j):
        assert i < j
        return s[:i] + s[(i+1):j] + s[(j+1):]

    def find_naive(self):
        all = set()

        for i in range(self.n):
            for j in range(i + 1, self.n):
                all.add(
                    self.remove(self.s, i, j)
                )

        return all

def reader():
    for l in sys.stdin:
        return l.strip()


if __name__ == '__main__':
    bs = BeautifulString(reader())
    solutions = bs.find_naive()
    print solutions
    print len(solutions)
