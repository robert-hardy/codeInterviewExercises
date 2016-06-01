def add(node, val):
    new_node = [ val, [], []]
    if node:
        left, right = node[1:]
        if not left:
            left.extend(new_node)
        elif not right:
            right.extend(new_node)
        else:
            add(left, val)
    else:
        node.extend(new_node)
    return node

def traverse_print(t, order):
    if not t:
        return
    print t[0]
    traverse_print(t[1], order)
    traverse_print(t[2], order)

def traverse_yield(t, order):
    if not t:
        return
    yield t[0]
    for l  in traverse_yield(t[1], order):
        yield l
    for r in traverse_yield(t[2], order):
        yield r

def traverse_global_var(t):
    def helper(t):
        if not t:
            return
        result.append(t[0])
        helper(t[1])
        helper(t[2])
    result = []
    helper(t)
    return result
