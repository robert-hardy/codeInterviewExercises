from bisect import bisect_left, bisect_right

def make_left_cts_step_function(step_points, plateaus):
    def left_cts_step_function(x):
        i = bisect_left(step_points, x)
        return plateaus[i]
    return left_cts_step_function

def cumulative_sum(lst):
    total = 0
    for x in lst:
        total += x
        yield total

def make_inv_dist_func(random_nums, probabilities):
    cumulative_probabilities = list(cumulative_sum(probabilities))
    return make_left_cts_step_function(cumulative_probabilities,
            random_nums)
