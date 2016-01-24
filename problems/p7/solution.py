from euler_projects.problems.p3.solution import PrimeDecomposition

def solve(n=10001):
    assert n >= 1
    p = PrimeDecomposition()

    for i in range(n+10):
        p.get_one_more_prime()

    return p.primes_list[n - 1]
