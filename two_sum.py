import itertools
from random import shuffle

def all_permutations(lst):
    return list(itertools.combinations(enumerate(lst), 2))

def get_first_sum_to_target(combos, target):
    for (x, y) in combos:
        if x[1] + y[1] == target:
            return (x, y)
    return None

if __name__ == '__main__':
    lst = list(range(10))
    shuffle(lst)
    print lst
    print get_first_sum_to_target(all_permutations(lst), 5)
