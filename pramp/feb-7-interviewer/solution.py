# solution.py
SOLUTION = '1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12'


class Clockwise:

    def __init__(self):
        self.data = self.load_data()
        self.n = len(self.data)
        self.m = len(self.data[0])
        self.nm = self.n * self.m
        self.spiral = []

    @staticmethod
    def load_data():
        data = []
        f = open('data.txt', 'r')
        for l in f:
            data.append(
                [s for s in l.strip().split(' ') if s != '']
            )
        return data

    def read(self):
        spiral = []

        # There are four edges to read

        """
        First edge
        n passes starts at 0
        row number n_passes
        Same row number, print range(n_passes, n - n_passes)
        """

        """
        Last column
        column number n - 1 - n_passes
        from row range(n_passes + 1, n - (n_passes + 1)
        """

        n_loops = 0
        while 2 * n_loops < self.n:

            # Do first row
            i = n_loops
            for j in range(n_loops, self.m - n_loops):
                spiral.append(
                    self.data[i][j]
                )

            # Do last column
            j = self.m - 1 - n_loops
            for i in range(n_loops + 1, self.n - (n_loops + 1)):
                spiral.append(
                    self.data[i][j]
                )

            # Do last row
            i = self.n - 1 - n_loops
            for j in range(self.m - n_loops - 1, n_loops - 1, -1):
                spiral.append(
                    self.data[i][j]
                )

            # Do first columns
            j = n_loops
            for i in range(self.n - (n_loops + 1) - 1, n_loops, -1):
                spiral.append(
                    self.data[i][j]
                )

            n_loops += 1

        self.spiral = spiral

    def print_spiral(self):
        print ' '.join(self.spiral)

    def solutions_check(self):
        return self.spiral == SOLUTION.split(' ')
