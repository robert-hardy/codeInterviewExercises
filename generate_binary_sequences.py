def gen():
    number = 2
    while True:
        yield bin(number)[3:]
        number = number + 1
