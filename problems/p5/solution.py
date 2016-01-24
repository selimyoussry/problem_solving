from euler_projects.problems.p3.solution import PrimeDecomposition


def solve(n):
    """
    Count the maximal number of occurrences of every prime number
    that appears in the decomposition of each number
    until n
    """
    p = PrimeDecomposition()

    decompositions = dict()
    for i in range(2, n + 1):
        decompositions[i] = p.decompose(i, [], 0)

    multiplicities = dict()
    for _, dec in decompositions.iteritems():
        primes_occurrences = occurrences(dec)
        for prime, prime_occurrences in primes_occurrences.iteritems():
            if prime in multiplicities:
                multiplicities[prime] = max(
                    multiplicities[prime],
                    prime_occurrences
                )
            else:
                multiplicities[prime] = prime_occurrences

    solution = 1
    for prime, multiplicity in multiplicities.iteritems():
        solution *= pow(prime, multiplicity)

    return solution

def occurrences(l):
    counts = dict()
    for e in l:
        if e in counts:
            counts[e] += 1
        else:
            counts[e] = 1
    return counts
