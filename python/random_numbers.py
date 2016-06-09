from bisect import bisect

def step_function(
        x,
        step_points=[60, 70, 80, 90],
        plateaus='FDCBA',
        right_cts=True):
    i = bisect(step_points, x)
    if not right_cts:
        i = max(0, i-1)
    return plateaus[i]
