# solution.py

class MinSteps:

    def __init__(self):
        self.values = {
            1: 0,
            2: 1,
            3: 1
        }
        self.max_value = 3

    def run(self, n):
        if n not in self.values:
            options = [n - 1]
            if n % 2 == 0:
                options.append(n / 2)
            if n % 3 == 0:
                options.append(n / 3)
            self.values[n] = min(
                map(lambda x: self.run(x), options)
            ) + 1

        return self.values[n]

    def run_bu(self, n):
        """
        bu stands for bottom up
        """
        for k in range(self.max_value + 1, n + 1):
            options = [self.values[k - 1]]
            if k % 2 == 0:
                options.append(self.values[k / 2])
            if k % 3 == 0:
                options.append(self.values[k / 3])
            self.values[k] = min(options) + 1
        self.max_value = n

        return self.values[n]
