import itertools

def all_permutations(lst):
    return list(itertools.combinations(enumerate(lst), 2))
