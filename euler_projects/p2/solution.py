PB_UPPER_LIMIT = 4 * 1000 * 1000

class Fibonacci:

    def __init__(self, mem=dict()):
        self.mem = mem

        # Initialize memory values
        self.mem[1] = 1
        self.mem[2] = 2

    def fib(self, n):
        """
        :param n: n_th number of fibonacci
        :return:
        """

        if n in self.mem.keys():
            return self.mem[n]
        elif (n-1) in self.mem.keys():
            ret = self.mem[n - 1] + self.mem[n - 2]
        else:
            ret_n_1 = self.fib(n-1)  # it should automatically compute mem[n - 2]
            ret = ret_n_1 + self.mem[n - 2]

        self.mem[n] = ret
        return ret

    def solve(self, upper_limit=PB_UPPER_LIMIT):
        n = 1
        cum_sum = 0

        while self.fib(n) <= upper_limit:

            if self.fib(n) % 2 == 0:
                cum_sum += self.fib(n)

            n += 1

        print 'Maximum n reached: {}'.format(n)

        return cum_sum
