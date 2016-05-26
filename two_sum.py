import itertools

def all_permutations(lst):
    return list(itertools.combinations(enumerate(lst), 2))

def get_first_sum_to_target(combos, target):
    for (x, y) in combos:
        if x[1] + y[1] == target:
            return (x, y)
    return None
