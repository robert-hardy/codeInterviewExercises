from itertools import (
    count,
    imap
)

def gen(nb_steps=1):
    number = 2 ** nb_steps
    return imap(lambda x: bin(x)[3:], count(number))
