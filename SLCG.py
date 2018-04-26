def SLCG(initialState, actions, startNode):
    lcgNodes = []
    lcgEdges = {}
    # processdictionary
    # targets = []
    # for i in actions.values():
    #    targets.append((i[0][1],i[0][3]))
    ls = [startNode]  # current node
    LS = set([])  # LS = set([startNode]) # traversed nodes
    while ls:
        i = ls[0]
        ls.pop(0)
        if i in LS:  # and [i] != LS:
            continue
        lcgNodes.append(i)
        LS = LS | {i}
        # if i[1] == initialState[i[0]]:
        if i in initialState.items():
            continue
        else:
            act = actions[i]
            # act = [actions[value] for value in targets if value == i]
            lcgEdges[i] = act
            for j in act:
                lcgNodes.append(j)
                # for m in j:
                lcgEdges[j] = list(j[0])
                # for k in j[0]:
                ls.extend(j[0])
    for i in lcgNodes:
        if i not in lcgEdges:
            lcgEdges[i] = []
    return lcgNodes, lcgEdges  # , solNodeArray
