# solution.py

class Pal:

    def __init__(self, N, d):
        self.N = N
        self.d = d

    @staticmethod
    def f(n, d, L):
        return (L+1)*(n**2) + d*n*L*(L+1) + (d**2)*L*(L+1)*(2*L+1)/6

    @staticmethod
    def is_palindrome(a):
        str_a = str(a)
        return str_a == str_a[::-1]

    def find_palindromes(self):

        sum_pal = 0
        palindromes = set()

        n = 1
        while n**2 + (n+self.d)**2 < self.N:

            cum_pal = n**2 + (n+self.d)**2
            k = 2
            while cum_pal < self.N:
                if self.is_palindrome(cum_pal) and cum_pal not in palindromes:
                    palindromes.add(cum_pal)
                    sum_pal += cum_pal
                cum_pal += ( (n + self.d * k) ** 2 )
                k += 1

            n += 1

        return sum_pal


import sys

first = True

for l in sys.stdin:
    if first:
        first = False
    else:
        N, d = map(lambda s:int(s), l.split(' '))
        pal = Pal(N,d)
        print pal.find_palindromes()