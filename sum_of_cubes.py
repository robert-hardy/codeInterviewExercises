import math

def go(n):
    solution = []
    for a in range(1, n+1):
        for b in range(1, a+1):
            for c in range(a+1, n+1):
                try:
                    d = int(math.pow(a**3 + b**3 - c**3, 1/3.0))
                    if a**3 + b**3 == c**3 + d**3:
                        solution.append((a, b, c, d))
                except:
                    pass
    return solution

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
