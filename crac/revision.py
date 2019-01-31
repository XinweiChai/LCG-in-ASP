import copy


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


def check(x, pass_item, to_check):
    for i in to_check:
        if i != pass_item and set(x) >= set(i):
            return True
    return False


def product(args):  # product for sets of sets
    result = [[]]
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


def cut_set(lcg_edges, rev_lcg_edge, lcg_nodes):  # use simplified lcg
    val = {}
    ranking = rank(lcg_edges)
    for i in ranking:
        val[i] = []
    while ranking:
        val_temp = update(val, ranking.pop(0), lcg_edges,
                          lcg_nodes)  # possible to use a subset of lcg_nodes to squeeze the result
        if val_temp != val:
            ranking = rev_lcg_edge[ranking[0]] + ranking
        val = val_temp
    return val


def update_completion(val, n, lcg_edges):
    if len(n) == 2:  # states
        for i in lcg_edges[n]:
            val[n] = val[n] + val[i]
    else:  # state
        temp = []
        for i in lcg_edges[n]:
            temp.append(val[i])
        if len(temp) > 0:
            val[n] = val[n] + product(temp)
        val[n] = [[n]] + val[n]  # suppose we can remove node n
    return val


def completion_set(lcg_edges, rev_lcg_edge, initial_state, lcg_nodes):
    val = {}
    ranking = rank(lcg_edges)
    for i in ranking:
        val[i] = []
    while ranking:
        val_temp = update(val, ranking.pop(0), lcg_edges, lcg_nodes)
        if val_temp != val:
            ranking = rev_lcg_edge[ranking[0]] + ranking
        val = val_temp
    return val


if __name__ == "__main__":
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
