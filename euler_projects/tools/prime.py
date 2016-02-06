__author__ = 'somedude'


class Prime:

    def __init__(self):
        self.primes = dict()
        self.divisors = dict()

    def erathosthene(self, maxi):
        """
        :type maxi: int
        :return:
        """

        for i in range(2, maxi):
