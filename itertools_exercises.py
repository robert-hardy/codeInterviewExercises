from itertools import (
    count,
    imap,
    groupby
)

def tabulate(func):
    return imap(func, count())

def separate_the_a(s):
    def is_a(letter):
        return letter == 'a'
    result = []
    for k,g in groupby(s, is_a):
        result.append(list(g))
    return result
