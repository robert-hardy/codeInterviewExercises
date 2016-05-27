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
    if not t:
        return
    print t[0]
    traverse(t[1], order)
    traverse(t[2], order)
