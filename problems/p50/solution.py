from euler_projects.problems.p10.erathosthene import Eratho

class PrimeSum:

    def __init__(self, maxi):
        self.maxi = maxi

        self.e = Eratho(self.maxi, crible=True)
        self.primes = self.e.get_primes()

        self.maximum_length = self.find_maximum_length()

    def find_maximum_length(self):
        i = 0
        cumsum = self.primes[i]
        while cumsum < self.primes[-1]:
            i += 1
            cumsum += self.primes[i]

        return i

    def try_length(self, l):
        first = 0
        last = l
        cumsum = sum(self.primes[first:last])

        while cumsum <= self.maxi and not self.e.primes[cumsum] and last < self.maxi:
            cumsum = cumsum - self.primes[first] + self.primes[last]
            first += 1
            last += 1

        if cumsum <= self.maxi and self.e.primes[cumsum]:
            return first, last, self.primes[first], self.primes[last], cumsum
        else:
            return False
