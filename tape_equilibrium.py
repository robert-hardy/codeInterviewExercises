def all_slices(lst):
    return [ ( lst[:i], lst[i:] ) for i in iter(lst[1:]) ]

def make_sums(tuples_of_lists):
    return [ (sum(a), sum(b)) for (a, b) in tuples_of_lists ]
