import itertools

def tabulate(func):
    return itertools.imap(func, itertools.count())
