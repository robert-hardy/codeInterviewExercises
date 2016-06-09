from bisect import bisect

def step_function(x, step_points=[60, 70, 80, 90], plateaus='FDCBA'):
    i = bisect(step_points, x)
    return plateaus[i]
