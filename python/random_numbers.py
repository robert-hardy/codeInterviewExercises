from random import randint

def collect_many_random_integers():
    return set([randint(0,9) for x in range(200)])
