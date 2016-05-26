import itertools

def all_permutations(lst):
    return list(itertools.permutations(enumerate(lst), 2))
