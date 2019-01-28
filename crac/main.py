from partial_corr import *
from models import *
from tools import *
from test import *
from reachability import *
# import itertools
# import pypint
import os

num_var = 10
period = 8
up_threshold = 0.8
down_threshold = 0.2
delay = 1
noise = 0
maxsize = 5
# file_name = "test_model1.an"
# goal = "a=1"

# eq, ts, discrete_ts, partial_matrix, above_threshold, below_threshold = random_test(num_var, period, up_threshold, down_threshold, noise)
# print(consistent_rate(eq, partial_matrix, threshold))
# print(consistent_rate2(eq, partial_matrix, threshold))

# print(one_run_over_approximation('test_model', [], ('n1', '1')))
# print(one_run_recursive('test_model1.an', [], ('a', '1'), below_threshold, above_threshold))

a = ([1, 7], [2, 3])
b = ([1, 4], [5], [6])
c = ([5], [6])
e = (a, b, c)
print(product_t(a, b))
print(product(e))
# print(product_alter(e))
#
# a = (1, 2)
# b = (3, 4)
# c = (5, 6)
# e = (a, b)
# print((product2(e)))

# m = pypint.load("test_model.an")
# res = m.cutsets(goal="n1=1", maxsize=5, exclude=[], exclude_initial_state=False, exclude_goal_automata=True,
#                timeout=None)
# res = m.cutsets(goal="n1=1", maxsize=10, exclude_initial_state=False, exclude_goal_automata=False, timeout=None)
# res = os.system("pint-reach --cutsets " + str(maxsize) + " " + goal + " -i " + file_name)
# print(res)
