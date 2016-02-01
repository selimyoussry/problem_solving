from prime_numbers import main


class Amicable:

    def __init__(self, until=10000):
        self.until = until
        self.p = main.Prime(self.until)
        self.divisors_sum = self.get_divisors_sum()
        self.amicables = []

        self.find_amicable_numbers()

    def get_divisors_sum(self):
        out = dict()
        for number, d in self.p.prime_divisors.iteritems():
            out[number] = sum(d.get_all_divisors()) - number
        return out

    def is_amicable(self, a):
        b = self.divisors_sum[a]
        if b not in self.divisors_sum:
            return False

        return self.divisors_sum[b] == a and b != a

    def find_amicable_numbers(self):
        for number in range(2, self.until):
            if self.is_amicable(number):
                self.amicables.append(number)
                self.amicables.append(self.divisors_sum[number])

        self.amicables = list(set(self.amicables))

    def solve(self):
        return sum(self.amicables)
