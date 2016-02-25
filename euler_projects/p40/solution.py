# solution.py

def generate_str(maxi):

    s = ''.join(map(str, range(1, maxi + 1)))
    return s

def solve():
    s = generate_str(1 * 1000 * 1000)
    multipliers = []
    for i in range(1, 6 + 1):
        multipliers.append(int(s[pow(10, i) - 1]))

    print s
    print multipliers

    out = 1
    for elt in multipliers:
        out *= elt

    return out
