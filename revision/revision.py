from batch_test import *
from cycle import *


def pre_check(f_network, reach, unreach, actions, actions_by_hitter, initial_state, start_node):
    reach_set = []
    unreach_set = []  # unsatisfied set
    L = {}
    dict_lcg = {}

    for i in reach + unreach:
        # Maybe can be replaced by logic programs
        [lcg_nodes, lcg_edges] = slcg(initial_state, actions, i)
        lcg_edges = cycle(lcg_nodes, lcg_edges, start_node, actions_by_hitter, actions)
        dict_lcg[i] = [lcg_nodes, lcg_edges]
        L[i] = [i]
        for j in lcg_nodes:
            if j in reach + unreach:
                L[i].append(j)
        res, x = one_run(f_network, i[0], i[1], i[2])
        if not res and i in reach:
            unreach_set.append(i)
        if res and i in unreach:
            reach_set.append(i)
    return reach_set, unreach_set, L, dict_lcg


def specialize(f_network, actions, initial_state, reach, unreach, to_revise, dict_lcg):
    rev = [to_revise]
    for i in rev:
        res = one_run_no_timer(f_network, initial_state, j)  # reachability, iterations, sequence
        trans = []
        # get the used transition
        mark = False
        for j in unreach:
            if j not in trans[0]:
                mark = True
                break
        if mark:
            for k in actions[to_revise]:
                if k == trans:
                    k[0].append(j)
                    return k[0], actions
        else:

    # check all the local states besides initial states, if not possible, create a self-dependence



def generalize(f_network, actions, initial_state, reach, unreach, to_revise, dict_lcg):
    for i in actions[to_revise]:
        mark = False
        for j in i[0]:
            if j in unreach:
                mark = True
                i[0].remove(j)
        if mark:
            break
    if mark:
        return i[0], actions
    else:
        for i in actions[to_revise]:
            mark = False
            for j in i[0]:
                res = one_run_no_timer(f_network, initial_state, j)
                if not res[0]:
                    mark = True
                    i[0].remove(j)
            if mark:
                return i[0], actions
        if mark:
            return i[0], actions
    return 1


# def dependency_tree(start_node, lcg_edges, reach, unreach):
#     tree = {}
#     # build LCG for each element and check if there are other elements included
#     return tree


def overall(f_network, lcg_edges, reach, unreach):
    for i in reach:
        if i in unreach:
            return None  # conflicted input
    [dictionary, actions, actions_by_hitter, initial_state, start_node] = read_ban(f_network)
    # acquire Re and Un
    [reach_set, unreach_set, L, dict_lcg] = pre_check(f_network, reach, unreach, actions, actions_by_hitter,
                                                      initial_state, start_node)
    # if there are unbreakable cycles, abandon
    if not reach_set and not unreach_set:
        return None
    while L:
        L_sorted = sorted(L.items(), key=lambda item: len(item[1]))
        for i in L_sorted:
            # reconstruct lcg)
            res, x = one_run(f_network, i[0], i[1], i[2])
            if (i in reach_set and res) or (i in unreach_set and not res):
                L.pop(i)
                continue
            if i in reach_set:
                generalize(f_network, actions, initial_state, reach, unreach, i, dict_lcg)
            else:
                specialize()
            L.pop(i)
    return lcg_edges
