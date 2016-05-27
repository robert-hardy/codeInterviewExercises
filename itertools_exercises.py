import itertools

def tabulate(func):
    for i in itertools.count():
        yield func(i)
