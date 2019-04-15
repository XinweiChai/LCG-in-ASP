from read_ban import *
from SLCG import *
from cycle import *
from precodition import *
from heuristics import *
from itertools import product
import multiprocessing
import time


def batch(fn, f_network):  # comparison with Pint and PermReach
    fo = open(f_network + "_out", 'w')
    if fn:
        f = open(fn, 'r')
        input_init = re.split(' ', f.readline().replace("\n", ""))
        output = re.split(' ', f.readline().replace("\n", ""))
        f.close()
    else:
        [dictionary, _, _, _, _] = read_ban(f_network)
        input_init = dictionary
        output = dictionary
    for i in product([0, 1], repeat=len(input_init)):
        fo.write("--- ")
        for k in range(len(i) - 1):
            fo.write(input_init[k] + "=" + str(i[k]) + ", ")
        fo.write(input_init[-1] + "=" + str(i[-1]) + "\n")
        # fo.writelines(str(i)+"\n")
        for j in output:
            output_file(fo, f_network, input_init, i, j)
    fo.close()


def output_file(f_out, f_network, input_instance, i, j):
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    p = multiprocessing.Process(target=one_run, args=(f_network, input_instance, i, (j, '1'), return_dict))
    p.start()
    # Wait 30 seconds for one_run
    p.join(30)
    # Terminate one_run
    if p.is_alive():
        p.terminate()
        f_out.writelines("Timeout\n")
        p.join()
        return [False, 10000]
    # Cleanup
    [boo, iterations] = [return_dict[0][0], return_dict[0][1]]
    p.join()
    # [boo, iterations] = one_run(f_network, input_instance, i, (j, '1'))
    # return_dict[0] = [boo, iterations]
    f_out.writelines("# " + j + "=1\n")
    if boo:
        f_out.writelines("True\n")
    elif iterations == 0 or iterations == 1:
        f_out.writelines("False\n")
    else:
        f_out.writelines("Inconclusive, " + str(iterations) + " iterations\n")
    return return_dict[0]
    # return boo, iterations


def iteration_test(f_network, f_out):  # count the average and max iteration
    fo = open(f_out + '.out', 'w')
    if f_network:
        f = open(f_network, 'r')
        input_init = re.split(' ', f.readline().replace("\n", ""))
        output = re.split(' ', f.readline().replace("\n", ""))
        f.close()
    else:  # if no input_init and output, input_init and output are set to universe by default
        [dictionary, _, _, _, _] = read_ban(f_out)
        input_init = dictionary
        output = dictionary
    total_trial = 0
    reach_count = 0
    max_count = 0
    inc = 0
    for i in product([0, 1], repeat=len(input_init)):
        fo.write("--- ")
        for k in range(len(i) - 1):
            fo.write(input_init[k] + "=" + str(i[k]) + ", ")
        fo.write(input_init[-1] + "=" + str(i[-1]) + "\n")
        # fo.writelines(str(i)+"\n")
        for j in output:
            [res, iter] = output_file(fo, f_out, input_init, i, j)
            if res:
                total_trial = total_trial + iter
                if iter > max_count:
                    max_count = iter
                reach_count = reach_count + 1
            else:
                if iter > 1:
                    inc = inc + 1
    if reach_count == 0:
        return 0, max_count, inc
    else:
        average = total_trial / reach_count
        return average, max_count, inc


def test_models(begin, end):
    for i in range(begin, end):
        batch('', 'model' + str(i))


def batch_iteration_test(begin, end, fn, f_network):
    aver_of_average = 0
    max_of_max = 0
    aver_of_inc = 0
    for i in range(begin, end):
        print(i)
        average, max_count, inc = iteration_test(fn, f_network + str(i))
        aver_of_average = aver_of_average + average
        aver_of_inc = aver_of_inc + inc
        if max_count > max_of_max:
            max_of_max = max_count
    return aver_of_average / (end - begin), max_of_max, aver_of_inc / (end - begin)


def one_run(f_network, input_init, change_state, start, return_dict):
    [_, actions, actions_by_hitter, initial_state, _] = read_ban(f_network)
    if change_state:
        for i in input_init:
            initial_state[i] = str(change_state[input_init.index(i)])
    start_node = start
    [lcg_nodes, lcg_edges] = slcg(initial_state, actions, start_node)
    lcg_edges = cycle(lcg_nodes, lcg_edges, start_node, actions_by_hitter, actions)
    lcg_edges = precondition(lcg_edges, actions_by_hitter, initial_state)
    lcg_edges = prune(lcg_edges, start_node)
    print(start_node)
    print(initial_state)
    if initial_state[start_node[0]] == start_node[1]:
        return_dict[0] = [True, 0]
        # return True, 0
    if start_node not in lcg_edges:
        return_dict[0] = [False, 0]
    # return False, 0
    or_gates = []
    or_gates_items = []
    for i in lcg_edges:
        if len(i) == 2 and len(lcg_edges[i]) > 1:
            or_gates.append(i)
            or_gates_items.append(lcg_edges[i])
    # return exhaustive_reach(or_gates, or_gates_items, lcg_edges, start_node, initial_state)
    if len(or_gates) <= 10:
        return_dict[0] = exhaustive_reach(or_gates, or_gates_items, lcg_edges, start_node, initial_state)
    else:
        # return_dict[0] = heuristics_perm_reach(len(or_gates) * 100 + 1, lcg_edges, start_node, initial_state)
        # return heuristics_perm_reach(len(or_gates) * 100 + 1, lcg_edges, start_node, initial_state)
        # return heuristics(len(or_gates)*5+1, lcg_edges, start_node, initial_state)
        return_dict[0] = heuristics(len(or_gates) * 5 + 1, lcg_edges, start_node, initial_state)


def one_run_with_options(f_network, input_init, change_state, start, return_dict, option):
    dict_option = {
        0: "Full ASP",
        1: "ASPReach",
        2: "PermReach"
    }
    if option not in dict_option:
        return_dict[0] = [False, 9999]
    [_, actions, actions_by_hitter, initial_state, _] = read_ban(f_network)
    if change_state:
        for i in input_init:
            initial_state[i] = str(change_state[input_init.index(i)])
    start_node = start
    [lcg_nodes, lcg_edges] = slcg(initial_state, actions, start_node)
    lcg_edges = cycle(lcg_nodes, lcg_edges, start_node, actions_by_hitter, actions)
    lcg_edges = precondition(lcg_edges, actions_by_hitter, initial_state)
    lcg_edges = prune(lcg_edges, start_node)
    print(start_node)
    print(initial_state)
    if initial_state[start_node[0]] == start_node[1]:
        return_dict[0] = [True, 0]
        # return True, 0
    if start_node not in lcg_edges:
        return_dict[0] = [False, 0]
    # return False, 0
    or_gates = []
    or_gates_items = []
    for i in lcg_edges:
        if len(i) == 2 and len(lcg_edges[i]) > 1:
            or_gates.append(i)
            or_gates_items.append(lcg_edges[i])
    print(dict_option[option])
    if option == 0 or len(or_gates) <= 10:
        return_dict[0] = exhaustive_reach(or_gates, or_gates_items, lcg_edges, start_node, initial_state)
    else:
        if option == 1:
            return_dict[0] = heuristics(len(or_gates) * 5 + 1, lcg_edges, start_node, initial_state)
        if option == 2:
            return_dict[0] = heuristics_perm_reach(len(or_gates) * 100 + 1, lcg_edges, start_node, initial_state)


def one_run_no_timer(actions, actions_by_hitter, initial_state, init_state, start):
    # [dictionary, actions, actions_by_hitter, initial_state, start_node] = read_ban(f_network)
    if init_state:
        initial_state = init_state
    start_node = start
    lcg_nodes, lcg_edges = slcg(initial_state, actions, start_node)
    lcg_edges = cycle(lcg_nodes, lcg_edges, start_node, actions_by_hitter, actions)
    lcg_edges = precondition(lcg_edges, initial_state)
    lcg_edges = prune(lcg_edges, start_node)
    # print(start_node)
    # print(initial_state)
    if initial_state[start_node[0]] == start_node[1]:
        return True, 0, [], lcg_edges
    if start_node not in lcg_edges:
        return False, 0, [], lcg_edges
    or_gates = []
    or_gates_items = []
    for i in lcg_edges:
        if len(i) == 2 and len(lcg_edges[i]) > 1:
            or_gates.append(i)
            or_gates_items.append(lcg_edges[i])
    if len(or_gates) <= 10:
        return exhaustive_reach(or_gates, or_gates_items, lcg_edges, start_node, initial_state)
    else:
        return heuristics(len(or_gates) * 5 + 1, lcg_edges, start_node, initial_state)


def one_run_over_approximation(f_network, init_state, start):
    [_, actions, actions_by_hitter, initial_state, _] = read_ban(f_network)
    if init_state:
        initial_state = init_state
    start_node = start
    [lcg_nodes, lcg_edges] = slcg(initial_state, actions, start_node)
    lcg_edges = cycle(lcg_nodes, lcg_edges, start_node, actions_by_hitter, actions)
    lcg_edges = precondition(lcg_edges, actions_by_hitter, initial_state)
    lcg_edges = prune(lcg_edges, start_node)
    print(start_node)
    print(initial_state)
    if initial_state[start_node[0]] == start_node[1]:
        return True
    if start_node not in lcg_edges:
        return False
    return True


def one_run_under_approximation(f_network, init_state, start):
    return True


if __name__ == "__main__":
    batch('data//data_tcr', 'data//tcrsig94.an')
    batch('data//data_egfr', 'data//egfr104.an')
    batch('', 'testPhage.an')
