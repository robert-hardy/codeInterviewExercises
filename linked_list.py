class ll(object):
    def __init__(self, lst):
        final_node = li(None, None)
        current_node = final_node
        for x in lst:
            new_node = li(x, current_node)
            current_node = new_node
        self.head = current_node

    def value(self):
        return self.head.value()

    def next(self):
        next_li = self.head.next()
        self.head = next_li

class li(object):
    def __init__(self, value, ni):
        self.val = value
        self.ni = ni

    def value(self):
        return self.val

    def next(self):
        return self.ni
