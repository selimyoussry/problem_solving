## This is the text editor interface. 
## Anything you type or change here will be seen by the other person in real time.

"""
Conventions

"""
import random


unbiased_coin = 0
biased_coin = 1

heads = 0
tail = 1


bag = [unbiased_coin] * 99 + [biased_coin] * 1

def select_coin(bag):
    return random.sample(bag, 1)[0]

def flip(coin):
    if coin == biased_coin:
        return heads
    else:
        return int(random.random() < 0.5)

def experiment():
    s = 0
    coin = select_coin(bag)
    for i in range(10):
        s += flip(coin)
    return coin, s

def simulation(n_experiments):

    coins = []
    for i in range(n_experiments):

        coin, s = experiment()
        if s == 0:
            coins.append(coin)

    return coins

def estimate_probability(coins):
    print coins[:10]
    n_biased = len([c for c in coins if c == biased_coin])
    n = len(coins)
    proba = float(n_biased) / n * 100
    return n_biased, n, proba


n_experiments = 1000 * 1000
coins = simulation(n_experiments)
print estimate_probability(coins)