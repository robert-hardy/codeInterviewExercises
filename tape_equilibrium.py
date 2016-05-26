def all_slices(lst):
    return [ ( lst[:i], lst[i:] ) for i in iter(lst[1:]) ]
