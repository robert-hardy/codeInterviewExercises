def gen():
    number = 0
    while True:
        yield bin(number)[2:]
        number =+ number
