class li(object):
    def __init__(self, value, ni):
        self.val = value
        self.ni = ni

    def value(self):
        return self.val

    def next(self):
        if self.ni is None:
            return self
        return self.ni

def create_ll(lst):
    tail = li(None, None)
    for x in lst[::-1]:
        new_head = li(x, tail)
        tail = new_head
    return new_head

def remove_duplicates(ll):
    vals = ""
    head = ll
    while head.value() is not None:
        vals = vals + ll.value()
        head = head.next()
    return create_ll(vals)
