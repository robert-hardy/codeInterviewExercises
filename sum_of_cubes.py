def find_one_pair():
    triangle = create_triangle()
    count = dict()
    for (a, b) in triangle:
        x = a^3+b^3
        if x in count:
            count[x].append((a,b))
        else:
            count[x] = [(a,b)]
    return { x: count[x] for x in count if len(count[x]) != 1 }

def create_triangle():
    lst = range(1000)
    triangle = [ (a, b) for a in lst for b in lst if b <= a ]
    return triangle
