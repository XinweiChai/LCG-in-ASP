def slcg(initial_state, actions, start_node):
    lcg_nodes = []
    lcg_edges = {}
    # targets = []
    # for i in actions.values():
    #    targets.append((i[0][1],i[0][3]))
    ls = [start_node]  # current node
    traversed_ls = set([])  # LS = set([start_node]) # traversed nodes
    while ls:
        i = ls[0]
        ls.pop(0)
        if i in traversed_ls:  # and [i] != LS:
            continue
        lcg_nodes.append(i)
        traversed_ls = traversed_ls | {i}
        if i in initial_state.items():
            continue
        else:
            act = actions[i]
            # act = [actions[value] for value in targets if value == i]
            lcg_edges[i] = act
            for j in act:
                lcg_nodes.append(j)
                # for m in j:
                lcg_edges[j] = list(j[0])
                # for k in j[0]:
                ls.extend(j[0])
    for i in lcg_nodes:
        if i not in lcg_edges:
            lcg_edges[i] = []
    return lcg_nodes, lcg_edges  # , solNodeArray
