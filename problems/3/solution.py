import numpy as np
from collections import OrderedDict


class PrimeDecomposition:

    def __init__(self):
        self.primes = OrderedDict([(2, True)])
        self.primes_list = [2]

    def is_prime(self, i):
        max_prime_known = self.primes.keys()[-1]
        max_bound = int(np.ceil(np.sqrt(max_prime_known)))
        we_think_is_prime = True

        known_primes = self.get_known_primes()
        len_known_primes = len(known_primes)
        j = 0
        while we_think_is_prime and j < len_known_primes and known_primes[j] <= max_bound:
            if i % known_primes[j] == 0:
                we_think_is_prime = False

            j += 1

        if we_think_is_prime:
            self.primes[i] = True
            self.primes_list.append(i)

        return we_think_is_prime

    def get_primes_until(self, k):
        max_prime_known = self.primes_list[-1]
        for i in range(max_prime_known + 1, k + 1):
            self.is_prime(i)

    def get_one_more_prime(self):
        i = self.primes_list[-1] + 1
        while not self.is_prime(i):
            i += 1

    def get_known_primes(self):
        return self.primes.keys()

    def decompose(self, n, dec, start_from):
        """
        :return: returns the largest prime factor of n
        """
        if n in self.primes or n == 1:
            dec.append(n)
            return dec
        else:
            if start_from == len(self.primes):
                self.get_one_more_prime()
            shift_start_from = 0

            for p in self.primes_list[start_from:]:
                if n % p == 0:
                    dec.append(p)
                    return self.decompose(
                        n=n / p,
                        start_from=start_from + shift_start_from,
                        dec=dec
                    )

            # Case the list is not big enough
            while n % self.primes_list[-1] != 0:
                self.get_one_more_prime()
            return self.decompose(
                n=n,
                start_from=start_from + shift_start_from,
                dec=dec
            )
