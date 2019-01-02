from pyasp.asp import *
from reconstruct import *
from fact_generator import generate
from itertools import product, permutations
import copy


def heuristics(k, lcg_edges, start_node, initial_state):
    for i in range(1, k + 2):
        new_lcg_edges = random_reconstruct(lcg_edges, start_node)
        res, x = asp_solve(new_lcg_edges, initial_state, i)
        if res:
            return res, i
        # elif x == 0:
        #    return False, 1
    return False, k, new_lcg_edges


def asp_solve(lcg_edges, initial_state, iteration):
    if not lcg_edges:
        return False, 0
    generate(initial_state, lcg_edges)
    g_options = ''
    s_options = '1'
    solver = Gringo4Clasp(gringo_options=g_options, clasp_options=s_options)
    encoding = 'nested.lp'
    facts = 'fact.lp'
    result = solver.run([encoding, facts], collapseTerms=True, collapseAtoms=False)
    for s in result:
        if Term('unreachable') in s:
            return False, iteration
        if Term('reachable') in s:
            s.remove(Term('reachable'))
            return True, iteration, s.to_list()
    return False, iteration


def exhaustive_run(or_gates, or_gates_items, lcg_edges, start_node, initial_state):  # ASPReach
    if not or_gates:
        return asp_solve(lcg_edges, initial_state, 0)
    for i in product(*or_gates_items):
        lcg_edges_copy = copy.deepcopy(lcg_edges)
        for j in range(len(or_gates)):
            lcg_edges_copy[or_gates[j]] = [i[j]]
        lcg_edges_copy = prune(lcg_edges_copy, start_node)
        res = asp_solve(lcg_edges_copy, initial_state, 0)
        if res[0]:
            return True, 0, res[2], i
    return False, 0


def exhaustive_reach(or_gates, or_gates_items, lcg_nodes, lcg_edges, start_node, initial_state):  # PermReach
    if not or_gates:
        return asp_solve(lcg_edges, initial_state, 0)
    for i in product(*or_gates_items):
        lcg_edges_copy = copy.deepcopy(lcg_edges)
        for j in range(len(or_gates)):
            lcg_edges_copy[or_gates[j]] = [i[j]]
        lcg_edges_copy = prune(lcg_edges_copy, start_node)
        res = and_gate(lcg_nodes, lcg_edges_copy, start_node, initial_state)
        if res:
            return True, 0
    return False, 0


def prune(lcg_edges, start_node):
    modified = True
    while modified:
        modified = False
        temp = list(lcg_edges.keys())
        for i in temp:
            if i != start_node:
                mark = False
                for j in lcg_edges.values():
                    if i in j:
                        mark = True
                        break
                if not mark:
                    modified = True
                    del lcg_edges[i]
    return lcg_edges


def heuristics_perm_reach(k, lcg_nodes, lcg_edges, start_node, initial_state):
    if start_node in initial_state:
        return [True, 0]
    for i in range(k):
        new_lcg_edges = random_reconstruct(lcg_edges, start_node)
        if not new_lcg_edges:
            return [False, 1]
        if and_gate(lcg_nodes, new_lcg_edges, start_node, initial_state):
            return [True, i + 1]
    return [False, k]


def and_gate(lcg_nodes, lcg_edges, start_node, initial_state):
    and_gates = [i for i in lcg_edges if len(lcg_edges[i]) > 1]
    and_gates_dict = {}
    for i in and_gates:
        and_gates_dict[i] = []
        for j in lcg_edges[i]:
            temp = j
            while temp not in and_gates and lcg_edges[temp]:
                temp = lcg_edges[temp][0]
            if temp in and_gates:
                and_gates_dict[i].append(temp)
    leaves = [i for i in and_gates_dict if not and_gates_dict[i]]
    if not and_gates_dict:
        return True
    while leaves:
        for i in leaves:
            flag_leaf = False
            for j in permutations(i[0]):
                flag = True
                temp_state = initial_state
                for k in j:
                    [boo, state, sequence] = simple_branch(k, temp_state, lcg_edges)
                    if not boo:
                        flag = False
                        break
                    else:
                        temp_state = state
                if flag:
                    flag_leaf = True
                    initial_state = temp_state
                    initial_state[i[1]] = i[3]
                    break
            if not flag_leaf:
                return False
        for i in leaves:
            and_gates_dict.pop(i)
            for j in and_gates_dict:
                if i in and_gates_dict[j]:
                    and_gates_dict[j].remove(i)
        leaves = [i for i in and_gates_dict if not and_gates_dict[i]]
    return True


def simple_branch(target, state, lcg_edges):
    if state[target[0]] == target[1]:
        return True, state, None
    temp = lcg_edges[target]
    if not temp:
        return False, None, None
    temp = temp[0]
    sequence = [temp]
    count = 0
    while lcg_edges[temp]:
        count = count + 1
        temp = lcg_edges[temp][0]
        if count % 2 == 0:
            sequence.append(temp)
    list.reverse(sequence)
    for i in sequence:
        for j in i[0]:
            if state[j[0]] != j[1]:
                return False, None, None
            else:
                state[i[1]] = i[3]
    return True, state, sequence
