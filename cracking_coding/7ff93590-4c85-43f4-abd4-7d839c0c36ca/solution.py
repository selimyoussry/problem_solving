"""
solution.py
"""

class MyCubeSum:

    def __init__(self):
        self.trivial_solutions = []
        self.non_trivial_solutions = []

    def c_sum(self, x, y):
        return pow(x, 3) + pow(y, 3)

    def solve(self):

        mini = 0
        maxi = 1000
        non_trivial_solutions = []

        ab_sums = dict()
        for a in range(mini, maxi + 1):
            for b in range(a + 1, maxi + 1):
                ab_sum = self.c_sum(a, b)
                if ab_sum in ab_sums:
                    ab_sums[ab_sum].append((a, b))
                else:
                    ab_sums[ab_sum] = [(a, b)]

        for ab_sum, l in ab_sums.iteritems():
            for a, b in l:
                non_trivial_solutions.extend(
                    [
                        (a, b, c, d) for c, d in l
                    ]
                )

        # Now add the free_solutions
        trivial_solutions = [(a, a, a, a) for a in range(mini, maxi + 1)]
        for a, b, c, d in non_trivial_solutions:
            trivial_solutions.extend(
                [
                    (a, b, d, c),
                    (b, a, c, d),
                    (b, a, d, c)
                ]
            )

        self.trivial_solutions = trivial_solutions
        self.non_trivial_solutions = non_trivial_solutions

    def book_solution(self):
        n = 1000

        my_sums = dict()
        results = []

        for c in range(0, n + 1):
            for d in range(0, n + 1):

                result = self.c_sum(c, d)
                if result in my_sums:
                    my_sums[result].append((c, d))
                else:
                    my_sums[result] = [(c, d)]

        for result, l in my_sums.iteritems():
            for pair1 in l:
                for pair2 in l:
                    results.append((pair1, pair2))

        return results
