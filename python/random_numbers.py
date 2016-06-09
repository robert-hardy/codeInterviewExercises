from bisect import bisect_left, bisect_right

def make_right_cts_step_function(step_points, plateaus):
    def right_cts_step_function(x):
        i = bisect_right(step_points, x)
        return plateaus[i]
    return right_cts_step_function

def make_left_cts_step_function(step_points, plateaus):
    def left_cts_step_function(x):
        i = bisect_left(step_points, x)
        return plateaus[i]
    return left_cts_step_function
