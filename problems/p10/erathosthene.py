__author__ = 'somedude'

class Eratho:

    def __init__(self, maxi):
        self.maxi = maxi
        self.primes = dict()
        self.cribled = False

        for i in range(2, self.maxi + 1):
            self.primes[i] = True

    def crible(self):
        prime = 2
        while prime < self.maxi:
            for alpha in range(2, self.maxi / prime + 1):
                self.primes[alpha * prime] = False

            # Get the new prime number
            prime += 1
            while prime < self.maxi and not self.primes[prime]:
                prime += 1

        self.cribled = True

    def get_primes(self):
        assert self.cribled
        return sorted([k for k, b in self.primes.iteritems() if b])
