def create_triangle(n):
    return [ (a, b) for a in range(1, n+1) for b in range(1, n+1) if b <= a ]

def collect_sums(n):
    triangle = create_triangle(n)
    sums = dict()
    for (a, b) in triangle:
        sum = a**3 + b**3
        if sum in sums:
            sums[sum].append((a, b))
        else:
            sums[sum] = [(a, b)]
    return sums

def filter_dict(d):
    return { x: d[x] for x in d if len(d[x]) > 1 }

def order_dict(d):
    return sorted([ (x, d[x]) for x in d ], key = lambda x: len(x[1]))

def go_for_it(n):
    return filter_dict(collect_sums(n))

if __name__ == '__main__':
    print go_for_it(1000)
