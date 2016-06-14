import itertools

def solution(A):
    for a, b, c in itertools.combinations(enumerate(A), 3):
        if a[1] + b[1] > c[1]:
            return (a[0], b[0], c[0])
    return False
