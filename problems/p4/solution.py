

def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]

def solve():
    l = range(100, 1000)
    palindromes = []

    for i in l:
        for j in l:
            p = i * j
            if is_palindrome(p):
                palindromes.append(p)

    return sorted(palindromes)[-1]
