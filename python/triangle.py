import itertools

def solution(A):
    lst = sorted(A)
    for a, b, c in zip(lst, lst[1:], lst[2:]):
        if a + b > c:
            return 1
    return 0

def solution2(A):
    for a, b, c in itertools.combinations(A, 3):
        if a+b>c and a+c>b and b+c>a:
            return 1
    return 0
