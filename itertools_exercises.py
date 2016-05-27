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
    the_a_list = []
    the_other_list = []
    for k,g in groupby(s, is_a):
        if k:
            the_a_list.extend(list(g))
        else:
            the_other_list.extend(list(g))
    return [ ''.join(the_a_list), ''.join(the_other_list) ]
