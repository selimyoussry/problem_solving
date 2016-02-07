# solution.py

import sys


class BruteForce:
    def __init__(self):
        pass

    def gen_r(self, k):
        return int('1' * k)

    def find_a(self, n):
        k = 1
        while self.gen_r(k) % n >0:
            k += 1
        return k

    def get_between(self, n_min, n_max):
        for n in range(n_min, n_max + 1):
            if n % 2 > 0 and n % 5 > 0:
                print n, self.find_a(n)


class HackerRank:
    def __init__(self):
        pass

    def go(self):
        b = BruteForce()

        first_line = True
        for l in sys.stdin:
            if first_line:
                first_line = False
            else:
                print b.find_a(n=int(l))
