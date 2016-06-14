import itertools

def solution(A):
    for a, b, c in itertools.combinations(A, 3):
        if a + b > c:
            return 1
    return 0
