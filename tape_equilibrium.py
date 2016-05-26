def all_slices(iterable):
    return [ [ iterable[:i], iterable[i:] ] for i in iter(iterable[1:]) ]
