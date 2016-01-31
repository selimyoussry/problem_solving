def read():

    f = open('data', 'r')
    numbers = []

    for l in f:
        numbers.append(
            int(l)
        )

    return numbers

def solve(numbers):

    return str(
        sum(numbers)
    )[:10]
