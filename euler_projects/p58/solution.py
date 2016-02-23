# solution.py
import math


class Spiral:

    def __init__(self):
        self.n = 1
        self.u = 1
        self.v = 1
        self.w = 1
        self.z = 1
        self.dim = 1

        self.primes = [False, True]

        self.ratio = 1.0
        self.total_primes_diag = 0
        self.diag_size = 1

        self.prev_u = 2

    def update(self):

        new_n = self.n + 1

        self.prev_u = self.u

        self.dim = 2 * new_n - 1
        self.v = self.u + 1 + self.dim - 2
        self.w = self.v + self.dim - 1
        self.z = self.w + self.dim - 1
        self.u = self.z + self.dim - 1

        self.n = new_n

    @staticmethod
    def sieve(b):

        primes = [True] * (b + 1)
        primes[0], primes[1] = False, False

        for p in range(2, int(math.sqrt(b)) + 1):
            if primes[p]:
                k = p ** 2
                while k <= b:
                    primes[k] = False
                    k += p
        return primes

    def find(self):

        while self.ratio >= 0.1:
            self.update()
            self.primes = self.sieve(self.u)

            print 'n {} :: u {}, v {}, w {}, z {}'.format(self.n, self.u, self.v, self.w, self.z)

            for elt in [self.v, self.w, self.z, self.u]:
                self.total_primes_diag += (1 if self.primes[elt] else 0)

            self.diag_size += 4

            self.ratio = float(self.total_primes_diag) / self.diag_size

            print 'n={} / ratio={}/{}={}%'.format(self.n, self.total_primes_diag, self.diag_size, round(self.ratio, 2))
