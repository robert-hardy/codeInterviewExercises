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

def traverse(t, order):
    result = []
    if not t:
        return t
    return t
