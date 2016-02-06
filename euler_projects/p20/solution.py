def factorial_sum(n, n_digits):

    div_ = pow(10, n_digits)

    reste = 1

    for i in range(2, n):
        reste = (reste * i) % div_

    return reste

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def solve(n=100):
    digits = map(lambda u: int(u), str(factorial(n)).strip())
    return sum(digits)