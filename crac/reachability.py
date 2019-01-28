from cycle import *
from read_ban import *
from revision import *


def precondition(lcg_edges, initial_state):
    mark = True
    while mark:
        mark = False
        for i in list(lcg_edges):
            if not lcg_edges[i] and i not in initial_state.items():  # and len(i) == 4:
                lcg_edges.pop(i)
                mark = True
                continue
            if len(i) == 4:
                for k in lcg_edges[i]:
                    if k not in lcg_edges:
                        mark = True
                        lcg_edges.pop(i)
                        break
            elif len(i) == 2 and i not in initial_state.items():
                for k in lcg_edges[i]:
                    if k not in lcg_edges:
                        lcg_edges[i].remove(k)
                        mark = True
                        break
    return lcg_edges


def slcg(initial_state, actions, start_node):
    lcg_nodes = []
    lcg_edges = {}
    ls = [start_node]  # current node
    LS = set([])  # LS = set([start_node]) # traversed nodes
    while ls:
        i = ls[0]
        ls.pop(0)
        if i in LS:  # and [i] != LS:
            continue
        lcg_nodes.append(i)
        LS = LS | {i}
        if i in initial_state.items():
            continue
        else:
            act = actions[i]
            lcg_edges[i] = act
            for j in act:
                lcg_nodes.append(j)
                lcg_edges[j] = list(j[0])
                ls.extend(j[0])
    for i in lcg_nodes:
        if i not in lcg_edges:
            lcg_edges[i] = []
    return lcg_nodes, lcg_edges  # , solNodeArray


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


def reach_state(x, lcg_edges, init_state):
    if x in init_state.items():
        return True
    if x not in lcg_edges:
        return False
    if not lcg_edges[x]:
        return False
    for i in lcg_edges[x]:
        if reach_trans(i, lcg_edges, init_state):
            return True
    return False


def reach_trans(x, lcg_edges, init_state):
    # if not lcg_edges[x]:
    #    return False
    for i in lcg_edges[x]:
        if not reach_state(i, lcg_edges, init_state):
            return False
    return True


def one_run_over_approximation(f_network, init_state, start):
    [dictionary, actions, actions_by_hitter, initial_state, start_node] = read_ban(f_network)
    if init_state:
        initial_state = init_state
    start_node = start
    [lcg_nodes, lcg_edges] = slcg(initial_state, actions, start_node)
    lcg_edges = cycle(lcg_nodes, lcg_edges, start_node, actions_by_hitter, actions)
    lcg_no_cycle = copy.deepcopy(lcg_edges)
    lcg_edges = precondition(lcg_edges, initial_state)
    lcg_edges = prune(lcg_edges, start_node)
    print(start_node)
    print(initial_state)
    if initial_state[start_node[0]] == start_node[1]:
        return True, lcg_no_cycle
    if start_node not in lcg_edges:
        return False, lcg_no_cycle
    return True, lcg_no_cycle


def one_run_recursive(f_network, init_state, start, below_threshold, above_threshold):
    [dictionary, actions, actions_by_hitter, initial_state, start_node] = read_ban(f_network)
    if init_state:
        initial_state = init_state
    start_node = start
    [lcg_nodes, lcg_edges] = slcg(initial_state, actions, start_node)
    lcg_edges = cycle(lcg_nodes, lcg_edges, start_node, actions_by_hitter, actions)
    for i in list(lcg_edges.keys()):
        if len(i) == 4 and not lcg_edges[i]:  # transitions
            lcg_edges.pop(i)
    # x = rank(lcg_edges)
    rev = reverse(lcg_edges)
    x = cut_set(lcg_edges, rev, lcg_nodes, below_threshold)
    y = completion_set(lcg_edges, rev, initial_state, lcg_nodes, above_threshold)
    # print(start_node)
    # print(initial_state)
    return reach_state(start_node, lcg_edges, initial_state), lcg_edges, x, y
