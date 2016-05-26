def gen(nb_steps=1):
    number = 2 ** nb_steps
    while True:
        yield bin(number)[3:]
        number = number + 1
