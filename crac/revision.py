import copy
import read_ban
from cycle import *
from SLCG import *
from batch_test import one_run_no_timer


# import pypint


def reverse(lcg_edges):
    rev = {}
    for i in lcg_edges:
        rev[i] = []
    for i in lcg_edges:
        for j in lcg_edges[i]:
            rev[j].append(i)
    return rev


def rank(lcg_edges):  # suppose there is no scc, returns the topological rank of an SLCG
    rev_lcg_edges = reverse(lcg_edges)
    ranking = []
    # rank_num = 0
    to_check = []
    checked = []
    for i in lcg_edges:
        if not lcg_edges[i]:
            to_check.append(i)
    while to_check:
        for i in to_check:
            if i in checked:
                to_check.remove(i)
                continue
            flag = True
            for j in lcg_edges[i]:
                if j not in checked:
                    flag = False
                    break
            if flag:
                checked = [i] + checked
                to_check.remove(i)
                to_check = rev_lcg_edges[i] + to_check
                # rank_num = rank_num + 1
                # ranking[rank_num] = i
                ranking.append(i)
    return ranking


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def contain_set(x, in_set):
    for i in in_set:
        if set(x) <= set(i):
            return True
    return False


def product_alter(args):  # product for sets of sets
    result = [[]]
    for pool in args:
        temp = []
        temp_res = []
        for i in result:
            for j in pool:
                if i:
                    if set(i) <= set(j):
                        temp.append(j)
                    elif set(i) > set(j):
                        temp.append(i)
        for x in result:
            if contain_set(x, temp):
                continue
            for y in pool:
                if y in temp:
                    continue
                temp_res.append(x + y)
        result = temp_res
        result = temp + result
    for i in range(len(result)):
        result[i] = list(set(result[i]))
    return result


def check(current, pass_item, to_check):
    for i in to_check:
        if i != pass_item and set(current) >= set(i):
            return True
    return False


def product(args):  # product for sets of sets
    result = [[]]
    args.append([[]])
    for pool in args:
        temp_res = []
        for x in result:
            for y in pool:
                temp = list(set(x + y))
                if not check(temp, x, result):
                    temp_res.append(temp)
        result = temp_res
    return result


def product_t(a, b):  # product for 2 sets of sets
    result = []
    for item_a in a:
        for item_b in b:
            temp = list(set(item_a + item_b))
            if not (temp in result):
                result.append(temp)
    return result


def product2(args):  # product for sets of variables
    result = [[]]
    for pool in args:
        temp = []
        for x in result:
            for y in pool:
                temp.append(x + [y])
        result = temp
    return result


def update(val, n, lcg_edges, ref_set):
    if len(n) == 4:  # solution
        for i in lcg_edges[n]:
            val[n] = val[n] + val[i]
    else:  # state
        temp = []
        for i in lcg_edges[n]:
            temp.append(val[i])
        if len(temp) > 0:
            val[n] = val[n] + product(temp)
        if n in ref_set:  # Obs in cut set
            val[n] = [[n]] + val[n]
    return val


def update_transition(val, n, lcg_edges, ref_set):
    if len(n) == 4:  # solution
        for i in lcg_edges[n]:
            val[n] = val[n] + val[i]
        if n in ref_set:  # Obs in cut set
            val[n] = [[n]] + val[n]
    else:  # state
        temp = []
        for i in lcg_edges[n]:
            temp.append(val[i])
        if len(temp) > 0:
            val[n] = val[n] + product(temp)
    return val


def cut_set(lcg_edges, lcg_nodes):  # use simplified lcg
    val = {}
    rev_lcg_edge = reverse(lcg_edges)
    ranking = rank(lcg_edges)
    for i in ranking:
        val[i] = []
    while ranking:
        val_temp = update(val, ranking.pop(0), lcg_edges, lcg_nodes)  # could use a subset of lcg_nodes
        if val_temp != val:
            ranking = rev_lcg_edge[ranking[0]] + ranking
        val = val_temp
    return val


def cut_set_transition(lcg_edges, lcg_nodes):  # use simplified lcg
    val = {}
    rev_lcg_edge = reverse(lcg_edges)
    ranking = rank(lcg_edges)
    for i in ranking:
        val[i] = []
    while ranking:
        val_temp = update_transition(val, ranking.pop(0), lcg_edges, lcg_nodes)  # could use a subset of lcg_nodes
        if val_temp != val:
            ranking = rev_lcg_edge[ranking[0]] + ranking
        val = val_temp
    return val


"""
def cut_set_transition(cs, lcg_edges, start_node):
    cst = []
    rev = reverse(lcg_edges)
    for i in cs[start_node]:
        temp = []
        for j in i:
            # if not lcg_edges[j]:
            #     temp = []
            #     break
            if rev[j]:
                temp.append(rev[j])
        if temp:
            cst.append(temp)
    return cst
"""


def update_completion(val, n, lcg_edges, init_state):
    if len(n) == 4:  # solution
        temp = []
        for i in lcg_edges[n]:
            temp.append(val[i])
        if len(temp) > 0:
            val[n] = val[n] + product(temp)
    else:  # state
        for i in lcg_edges[n]:
            val[n] = val[n] + val[i]
        if n[1] == initial_state[n[0]]:
            val[n] = [[]]
        else:
            val[n] = [[n]] + val[n]  # has no successor and is not in initial state
    return val


def completion_set(lcg_edges, lcg_nodes, initial_state):
    val = {}
    ranking = rank(lcg_edges)
    rev_lcg_edge = reverse(lcg_edges)
    for i in ranking:
        val[i] = []
    while ranking:
        val_temp = update_completion(val, ranking.pop(0), lcg_edges, initial_state)
        if val_temp != val:
            ranking = rev_lcg_edge[ranking[0]] + ranking
        val = val_temp
    return val


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
        # Get rid of self-dependencies in SLCGs
        L_sorted = dict(sorted(L.items(), key=lambda item: len(item[1])))
        for i in L_sorted:
            if i not in reach_set + unreach_set:
                L[i] = [i]
                continue
            # reconstruct lcg
            res, _, _, _ = one_run_no_timer(actions, actions_by_hitter, initial_state, init_state="", start=i)
            if (i in reach_set and res) or (i in unreach_set and not res):
                L[i] = [i]
                continue
            scc_element = []
            for j in cycles:
                if i in j:
                    scc_element = j
                    break
            if i in reach_set:
                pass
                # add transitions
            else:
                # delete transitions
                pass

            L[i] = [i]
            [reach_set, unreach_set, L, dict_lcg] = pre_check(f_network, reach, unreach, actions, actions_by_hitter,
                                                              initial_state, start_node)
    return actions


if __name__ == "__main__":
    # a = ([1, 7], [2, 3])
    # b = ([1, 4], [5], [6])
    # c = ([5], [6])
    # e = (a, b, c)
    # f = [[[('b', '1')], [('c', '1')]], [[('b', '0')], [('d', '1')], [('b', '1')]]]
    # print(product_t(a, b))
    # print(product(e))
    # print(product_alter(e))
    # a = (1, 2)
    # b = (3, 4)
    # c = (5, 6)
    # e = (a, b)
    # print((product(e)))
    # print(product(f))
    # [process, actions, actions_by_hitter, initial_state, start_node] = read_ban.read_ban("test_model.an")
    # [process, actions, actions_by_hitter, initial_state, start_node] = read_ban.read_ban("test_model1.an")
    [process, actions, actions_by_hitter, initial_state, start_node] = read_ban.read_ban("test_model2.an")
    start_node = ('a', '1')
    [lcg_nodes, lcg_edges] = slcg(initial_state, actions, start_node)
    # x = cut_set(lcg_edges, lcg_nodes)
    # y = cut_set_transition(lcg_edges, lcg_nodes)
    x = completion_set(lcg_edges, lcg_nodes, initial_state)
    print(x)
    # print(y)
    # m = pypint.load("test_model1.an")
    # res = m.cutsets(goal="n1=1", maxsize=5, exclude=[], exclude_initial_state=False, exclude_goal_automata=True,
    #                timeout=None)
    # res = m.cutsets(goal="n1=1", maxsize=10, exclude_initial_state=False, exclude_goal_automata=False, timeout=None)
    # res = os.system("pint-reach --cutsets " + str(maxsize) + " " + goal + " -i " + file_name)
    # print(res)
