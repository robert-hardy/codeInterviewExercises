def add(node, val):
    new_node = [ val, [], []]
    if not node:
        node.extend(new_node)
    return node
