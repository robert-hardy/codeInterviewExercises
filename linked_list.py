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

    def set_next(self, ni):
        self.ni = ni

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
        if head.value() not in vals:
            vals = vals + head.value()
        head = head.next()
    return create_ll(vals)

def remove_duplicates_without_buffer(ll):
    ok_head = trim_duplicates_from_front(ll)
    head = ok_head
    while head.value() is not None:
        if is_in(head.value(), head.next()):
            head.set_next(head.next().next())
        head = head.next()
    return ok_head


def trim_duplicates_from_front(ll):
    head = ll
    while is_in(head.value(), head.next()):
        head = head.next()
    return head

def is_in(val, ll):
    head = ll
    while head.value() is not None:
        if head.value() == val:
            return True
        head = head.next()
    return False

def to_string(ll):
    vals = ""
    head = ll
    while head.value() is not None:
        vals = vals + head.value()
        head = head.next()
    return vals
