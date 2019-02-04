from batch_test import one_run_no_timer
from read_ban import read_ban
from cycle import *
from SLCG import slcg
import random
import os
import re
import copy


def read_reach(fn):
    reach = []
    fn = open(fn)
    for i in fn.readlines():
        i = i.replace("\n", "")
        reach.append(tuple(re.split("=", i)))
    return reach


def pre_check(f_network, reach, unreach, actions, actions_by_hitter, initial_state, start_node):
    reach_set = []
    unreach_set = []  # unsatisfied set
    L = {}
    dict_lcg = {}

    for i in reach + unreach:
        # Maybe ABAN can be replaced by logic programs
        [lcg_nodes, lcg_edges] = slcg(initial_state, actions, i)
        lcg_edges = cycle(lcg_nodes, lcg_edges, start_node, actions_by_hitter, actions)
        dict_lcg[i] = [lcg_nodes, lcg_edges]
        L[i] = []
        for j in lcg_nodes:
            if j in reach + unreach:
                L[i].append(j)
        # res, _, _, _ = one_run_no_timer(copy.deepcopy(actions), copy.deepcopy(actions_by_hitter), initial_state, init_state="", start=i)
        res, _, _, _ = one_run_no_timer(actions, actions_by_hitter, initial_state,
                                        init_state="", start=i)
        if not res and i in reach:
            reach_set.append(i)
        if res and i in unreach:
            unreach_set.append(i)
    return reach_set, unreach_set, L, dict_lcg


def subsume(a, b):
    return set(a[0]) <= set(b[0])


def delete_subsume(p, r):
    for i in p:
        if subsume(i, r):
            p.remove(i)
    return p


def specialize(f_network, process, actions, actions_by_hitter, initial_state, reach, unreach, to_revise, dict_lcg,
               scc_element):
    rev = [to_revise]
    modified = []
    for i in rev:
        res, _, x, lcg_edges = one_run_no_timer(actions, actions_by_hitter, initial_state, init_state="",
                                                start=i)  # reachability, iterations, sequence, used transition
        trans = []
        for l in actions[i]:
            if l in lcg_edges[i]:  # used transitions
                trans.append(l)
        # get the used transition
        # mark = False
        for j in unreach + scc_element:
            for k in trans:
                if j not in k[0] and j != (k[1], k[3]) and k in actions[i]:  # no self-regulation
                    temp = (tuple(list(k[0]) + [j]), k[1], k[2], k[3])
                    modified.append(temp)
                    actions[i].remove(k)
                    actions[i].append(temp)
                    for m in k[0]:
                        actions_by_hitter[m].remove(k)
                        actions_by_hitter[m].append(temp)
                    actions_by_hitter[j].append(temp)
        return actions, actions_by_hitter, modified
        # mark = True
        # break
        # if mark:
        #     for k in actions[to_revise]:
        #         if k in trans:
        #             k[0].append(j)
        #             return k[0], actions
        # else:  # check all the local states besides initial states, if not possible, create a self-dependence
        #     for j in process:
        #         for k in [0, 1]:
        #             if (j, k) not in initial_state:
        #                 res = one_run_no_timer(f_network, initial_state, (j, k))
        #                 if not res[0]:
        #                     for l in actions[i]:
        #                         if l in res[3]:  # used transitions
        #                             l[0].append((j, k))
        #                             return l, actions


def generalize(f_network, actions, actions_by_hitter, initial_state, reach, unreach, to_revise, dict_lcg, scc_element):
    modified = []
    for i in actions[to_revise]:
        mark = False
        if len(i[0]) > 1:
            for j in i[0]:
                if j in unreach + scc_element and i in actions[to_revise]:
                    mark = True
                    temp = list(i[0])
                    temp.remove(j)
                    temp = (tuple(temp), i[1], i[2], i[3])
                    modified.append(temp)
                    actions[to_revise].remove(i)
                    actions[to_revise].append(temp)
                    for m in i[0]:
                        actions_by_hitter[m].remove(i)
                        if m != j:
                            actions_by_hitter[m].append(temp)
        if mark:
            break
    return actions, actions_by_hitter, modified
    # else:
    #     for i in actions[to_revise]:
    #         mark = False
    #         for j in i[0]:
    #             res, _, x = one_run_no_timer(f_network, initial_state, j)
    #             if not res[0]:
    #                 mark = True
    #                 i[0].remove(j)
    #         if mark:
    #             return i[0], actions
    #     if mark:
    #         return i[0], actions
    # return 1


def overall(f_network, reach, unreach):
    for i in reach:
        if i in unreach:
            return None  # conflicted input
    [process, actions, actions_by_hitter, initial_state, start_node] = read_ban(f_network)
    # acquire Re and Un
    [reach_set, unreach_set, L, dict_lcg] = pre_check(f_network, reach, unreach, actions, actions_by_hitter,
                                                      initial_state, start_node)
    # if there are unbreakable cycles, abandon
    if not reach_set and not unreach_set:
        return None
    modified = [1]
    while L and modified:
        modified = []
        scc = list(strongly_connected_components_path(L.keys(), L))
        cycles = copy.deepcopy(scc)
        for x in scc:
            if len(x) > 1:
                for element in x:
                    for succ in L[element]:
                        if succ in x and succ != element:
                            L[element].remove(succ)
            else:
                cycles.remove(x)
        L_sorted = dict(sorted(L.items(), key=lambda item: len(item[1])))
        for i in L_sorted:
            if i not in reach_set + unreach_set:
                L.pop(i)
                continue
            # reconstruct lcg
            res, _, _, _ = one_run_no_timer(actions, actions_by_hitter, initial_state, init_state="", start=i)
            if (i in reach_set and res) or (i in unreach_set and not res):
                L.pop(i)
                continue
            scc_element = []
            for j in cycles:
                if i in j:
                    scc_element = j
                    break
            if i in reach_set:
                actions, actions_by_hitter, modified = generalize(f_network, actions, actions_by_hitter, initial_state, reach,
                                                           unreach, i, dict_lcg, scc_element)
            else:
                actions, actions_by_hitter, modified = specialize(f_network, process, actions, actions_by_hitter,
                                                           initial_state, reach, unreach, i, dict_lcg, scc_element)
            L.pop(i)
            [reach_set, unreach_set, L, dict_lcg] = pre_check(f_network, reach, unreach, actions, actions_by_hitter,
                                                              initial_state, start_node)
    return actions


def rev_overall(p, re, un):
    # check reachability and
    return p


def generate_reach(p, var, input):
    # reach = batch(input, p)  # reachability
    # return reach
    return None


def partial_model(p, percentage):
    to_del = percentage * len(p)
    deleted = []
    for i in range(to_del):
        deleted.append(p.pop(random.randint(len(p))))
    return p, deleted


def state_change(trans):
    for i in trans[0]:
        for j in trans[1]:
            if i != j:
                return i
    return None


def consistent_trans(trans, rules):
    for i in rules:
        if i[0] == state_change(trans) and set(i[1]) <= set(trans[1]):
            return True
    return False


def consistent_model(p, tsd):  # see if all the transitions can be explained by rules
    for i in tsd:
        flag = False
        for j in p:
            if consistent_trans(i, j):
                flag = True
                break
        if not flag:
            return False
    return True


if __name__ == "__main__":
    # input_fn = 'output1'
    # output_fn = 'test'

    # model = os.system('./AS_LF1T.exe -i ' + input_fn + ' > ' + output_fn)
    [process, actions, actions_by_hitter, initial_state, start_node] = read_ban("example.an")
    reach = read_reach("Re")
    unreach = read_reach("Un")
    # reach_set, unreach_set, L, dict_lcg = pre_check("example.an", "Re", "Un", actions, actions_by_hitter, initial_state,
    #                                                 start_node)
    modified_actions = overall("example.an", reach, unreach)
    print(modified_actions)
