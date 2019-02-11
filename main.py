from batch_test import *
from generate_model import *
from timeit import default_timer
import math
import m2rit.util
import crac.revision
"""
# reachability test
sizes1 = list(range(10, 100, 10))
sizes2 = list(range(100, 100, 1001))
sizes = sizes1 + sizes2
size_density = 3
times = [1, 2, 3, 4, 5, 6, 7]
num_tran_var = size_density * times
models = 10
iteration = 50
automata = 20

time_recorder = {}
if __name__ == '__main__':
    f = open("data//runtime", 'w')
    for i in sizes:
        print(i)
        num_tran = size_density * i
        generate_files(models, i, num_tran)
        start = default_timer()
        for j in range(models):
            batch("data//inputFile", "data//model_" + str(i) + "//model_" + str(j))
        stop = default_timer()
        time_recorder[i] = (stop - start) / models / 20
        f.write(str(i) + ":" + str(time_recorder[i]) + '\n')
"""


def checkall(process, actions, actions_by_hitter, initial_state):  # test the reachability 0 -> 1
    re = []
    un = []
    for i in process:
        res, _, _, _ = one_run_no_timer(actions, actions_by_hitter, initial_state, [], (i, '1'))
        if res:
            re.append((i, '1'))
        else:
            un.append((i, '1'))
    return re, un


size = 50
density = 3
num_tran = size * density
cut_percentage = 0.2

# CRAC test
if __name__ == '__main__':
    transition_set = generate_random_an(size, num_tran)
    write_file(transition_set, "crac//complete_model", size)
    transition_set = transition_set[0: len(transition_set) - math.ceil(cut_percentage * len(transition_set))]
    write_file(transition_set, "crac//partial_model", size)
    process, actions, actions_by_hitter, initial_state, start_node = read_ban("crac//complete_model")
    re_complete, un_complete = checkall(process, actions, actions_by_hitter, initial_state)
    process, actions, actions_by_hitter, initial_state, start_node = read_ban("crac//partial_model")
    re_partial, un_partial = checkall(process, actions, actions_by_hitter, initial_state)
    actions = crac.revision.overall("crac//partial_model", re_complete, un_complete)

"""
# M2RIT test

if __name__ == '__main__':
    transition_set = generate_random_an(size, num_tran)
    write_file(transition_set, "m2rit//complete_model", size)
    transition_set = transition_set[0: len(transition_set) - math.ceil(cut_percentage * len(transition_set))]
    write_file(transition_set, "m2rit//partial_model", size)
    process, actions, actions_by_hitter, initial_state, start_node = read_ban("m2rit//complete_model")
    re_complete, un_complete = checkall(process, actions, actions_by_hitter, initial_state)
    process, actions, actions_by_hitter, initial_state, start_node = read_ban("m2rit//partial_model")
    re_partial, un_partial = checkall(process, actions, actions_by_hitter, initial_state)
    actions = m2rit.util.overall("m2rit//partial_model", re_complete, un_complete)
"""
