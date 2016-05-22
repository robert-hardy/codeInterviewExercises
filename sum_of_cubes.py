def find_one_pair():
    triangle = create_triangle()
    all_sums = [ a^3 + b^3 for (a, b) in triangle ]
    count = dict()
    for x in all_sums:
        if x in count:
            count[x] = count[x] + 1
        else:
            count[x] = 1
    return { x: count[x] for x in count if count[x] != 1 }

def create_triangle():
    lst = range(1000)
    triangle = [ (a, b) for a in lst for b in lst if b <= a ]
    return triangle
