class li(object):
    def __init__(self, value, ni):
        self.val = value
        self.ni = ni

    def value(self):
        return self.val

    def next(self):
        return self.ni

def create_ll(lst):
    tail = li(None, None)
    for x in lst:
        new_head = li(x, tail)
        tail = new_head
    return new_head
