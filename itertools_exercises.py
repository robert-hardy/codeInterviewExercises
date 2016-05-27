from itertools import (
    count,
    imap
)

def tabulate(func):
    return imap(func, count())
