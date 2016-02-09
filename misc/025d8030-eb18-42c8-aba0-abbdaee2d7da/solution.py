# solution.py


class Fibonacci:

    def __init__(self):
        self.values = {
            1: 1,
            2: 1
        }
        self.max_added = 2

    def run_dp(self, n):
        if n in self.values:
            return self.values[n]
        else:
            if ((n - 1) not in self.values) and ((n - 2) in self.values):
                self.values[n - 1] = self.values[n - 2] + self.values[n - 3]
            elif ((n - 1) not in self.values) and ((n - 2) not in self.values):
                self.run_dp(n - 1)

            self.values[n] = self.values[n - 1] + self.values[n - 2]
            return self.values[n]

    def run_dp_smarter(self, n):
        if n > self.max_added:
            # Find the first number not in self.values
            for k in range(self.max_added + 1, n + 1):
                self.values[k] = self.values[k - 1] + self.values[k - 2]
            self.max_added = n
        return self.values[n]

    def run_naive(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            return self.run_naive(n - 1) + self.run_naive(n - 2)
