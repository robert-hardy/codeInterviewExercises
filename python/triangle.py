import itertools

def solution(A):
    lst = sorted(A)
    for a, b, c in zip(lst, lst[1:], lst[2:]):
        if a + b > c:
            return 1
    return 0
