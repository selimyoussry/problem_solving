from prime_numbers import main as pn

def get_triangular_numbers(until=1000):
    return [n*(n+1) / 2 for n in range(2, until + 1)]

def solve(k, n_div, p=None):

    # Step 1 - Get the list of all prime numbers from 1 to 1 million, as well as all the numbers decomposition
    p = pn.Prime(1 * k * 1000) if p is None else p

    ts = get_triangular_numbers(k * 2)

    for t in ts:
        if p.prime_divisors[t].count_all_divisors() > n_div:
            print t, p.prime_divisors[t].divisors.items(), p.prime_divisors[t].get_all_divisors()
            return p

    return p
