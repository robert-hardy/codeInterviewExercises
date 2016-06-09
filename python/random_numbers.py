from bisect import bisect_left, bisect_right

def step_function(
        x,
        step_points=[60, 70, 80, 90],
        plateaus='FDCBA',
        right_cts=True):
    if right_cts:
        i = bisect_right(step_points, x)
    else:
        i = bisect_left(step_points, x)
    return plateaus[i]

def make_right_cts_step_function( step_points, plateaus):
    def right_cts_step_function(x):
        i = bisect_right(step_points, x)
        return plateaus[i]
    return right_cts_step_function

def make_left_cts_step_function( step_points, plateaus):
    def left_cts_step_function(x):
        i = bisect_left(step_points, x)
        return plateaus[i]
    return left_cts_step_function
