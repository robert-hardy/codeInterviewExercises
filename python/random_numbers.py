from bisect import bisect_left
from random import random

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
    if cumulative_probabilities[-1] != 1:
        raise ValueError('Probabilities do not sum to 1')
    return make_left_cts_step_function(
            cumulative_probabilities,
            random_nums
    )

def make_generator(random_nums, probabilities):
    inv_dist_func = make_inv_dist_func(random_nums, probabilities)
    def gen():
        return inv_dist_func(random())
    return gen

class RandomGen(object):
    def __init__(self, random_nums, probabilities):
        self.random_nums = random_nums
        self.probabilities = probabilities
        self.generator = make_generator(random_nums, probabilities)

    def next_num(self):
        return self.generator()
