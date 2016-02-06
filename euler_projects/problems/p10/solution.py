from euler_projects.problems.p3.solution import PrimeDecomposition

def sum_prime(n):
    p = PrimeDecomposition()

    p.get_primes_until(n + 10)

    return sum(
        [p for p in p.primes_list if p <= n]
    )
