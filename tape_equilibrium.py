from random import shuffle

def all_slices(lst):
    return [ ( lst[:i], lst[i:] ) for i in range(1, len(lst)) ]

def make_sums(tuples_of_lists):
    return [ (sum(a), sum(b)) for (a, b) in tuples_of_lists ]

def make_abs_diff(list_of_tuples):
    return [ abs(a-b) for (a, b) in list_of_tuples ]

if __name__ == '__main__':
    lst = list(range(20))
    shuffle(lst)
    print "List is:"
    print lst
    print "Minimum is:"
    print min(make_abs_diff(make_sums(all_slices(lst))))
