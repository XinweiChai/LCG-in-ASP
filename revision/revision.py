from batch_test import *
from cycle import *


def pre_check(f_network, reach, unreach):
    reach_set = []
    unreach_set = []  # unsatisfied set
    L = {}
    dict_lcg = {}
    [dictionary, actions, actions_by_hitter, initial_state, start_node] = read_ban(f_network)
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


def specialize(an, reach, unreach, to_revise, dict_lcg):
    rev = {to_revise: []}






    for i in reach + unreach:
        for j in rev:
            if i[2] in dict_lcg(j):
                rev[i].append(j)
    size_count = 0
    while rev:
        for i in rev:
            if len(rev[i]) == size_count:
                specialize()
        size_count = size_count + 1
    return an


def generalize(an, reach, unreach, unreach1):
    return an


# def dependency_tree(start_node, lcg_edges, reach, unreach):
#     tree = {}
#     # build LCG for each element and check if there are other elements included
#     return tree


def overall(f_network, lcg_edges, reach, unreach):
    for i in reach:
        if i in unreach:
            return None  # conflicted input
    # acquire Re and Un
    [reach_set, unreach_set, L, dict_lcg] = pre_check(f_network, reach, unreach)
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
                generalize()
            else:
                specialize()
            L.pop(i)
    return lcg_edges
