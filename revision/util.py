from batch_test import one_run_no_timer
from read_ban import read_ban
from cycle import *
from SLCG import slcg
import random
import os
import re


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
        res, _, _, _ = one_run_no_timer(f_network, init_state="", start=i)
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


def specialize(f_network, process, actions, initial_state, reach, unreach, to_revise, dict_lcg):
    rev = [to_revise]
    modified = []
    for i in rev:
        res, _, x, lcg_edges = one_run_no_timer(f_network, initial_state,
                                                i)  # reachability, iterations, sequence, used transition
        trans = []
        for l in actions[i]:
            if l in lcg_edges[i]:  # used transitions
                trans.append(l)
        # get the used transition
        # mark = False
        for j in unreach:
            for k in trans:
                if j not in k[0] and j != (k[1], k[3]):  # no self-regulation
                    temp = (tuple(list(k[0]) + [j]), k[1], k[2], k[3])
                    modified.append(temp)
                    actions[i].remove(k)
                    actions[i].append(temp)
        return actions, modified
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
                res, _, x = one_run_no_timer(f_network, initial_state, j)
                if not res[0]:
                    mark = True
                    i[0].remove(j)
            if mark:
                return i[0], actions
        if mark:
            return i[0], actions
    return 1


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
    while L:
        L_sorted = dict(sorted(L.items(), key=lambda item: len(item[1])))
        for i in L_sorted:
            if i not in reach_set + unreach_set:
                L.remove(i)
                continue
            # reconstruct lcg
            res, _, _, _ = one_run_no_timer(f_network, "", i)
            if (i in reach_set and res) or (i in unreach_set and not res):
                L.pop(i)
                continue
            if i in reach_set:
                generalize(f_network, actions, initial_state, reach, unreach, i, dict_lcg)
            else:
                actions, _ = specialize(f_network, process, actions, initial_state, reach, unreach, i, dict_lcg)
            L.pop(i)
            [reach_set, unreach_set, L, dict_lcg] = pre_check(f_network, reach, unreach, actions, actions_by_hitter,
                                                              initial_state, start_node)
    return f_network


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
    overall("example.an", reach, unreach)
