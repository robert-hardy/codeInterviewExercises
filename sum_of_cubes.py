def find_one_pair():
    lst = range(100)
    all_sums = [ a^3 + b^3 for a in lst for b in lst ]
    all_sums = sorted(all_sums)
    count = dict()
    for x in all_sums:
        if x in count:
            return x
        count[x] = 1
    return None
