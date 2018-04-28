from SCC import strongly_connected_components_path


def breakCycle(lcgEdges, scc, startNode, actionsByHitter, actions):
    if startNode in scc:
        lcgEdges = deleteElememt(startNode, scc, lcgEdges, actions, actionsByHitter)
    else:
        for i in scc:
            if len(i) == 2:
                for j in actionsByHitter[i]:
                    # for k in j[0]:
                    for k in (j[1], j[3]):
                        if k not in scc:
                            lcgEdges = deleteElememt(i, scc, lcgEdges, actions, actionsByHitter)
                            return lcgEdges
    return lcgEdges


def deleteElememt(element, scc, lcgEdges, actions, actionsByHitter):
    for i in scc:
        if i in actionsByHitter[element]:
            # lcgEdges[i].remove(element)
            lcgEdges[i] = []
            actions[(i[1], i[3])].remove(i)
            # for j in scc:
            #    if len(j)==2:
            #        if i in actions[j]:
            #            lcgEdges[j].remove(i)

    # lcgEdges[actionsByHitter[element]] = []  # delete the link of preceding action->element
    # lcgEdges[(
    # actions[element][1], actions[element][3])] = []  # delete the link of pred of preceding action -> preceding action
    return lcgEdges


def cycle(lcgNodes, lcgEdges, startNode, actionsByHitter, actions):
    cycle = True
    while cycle:
        cycle = False
        SCC = strongly_connected_components_path(lcgNodes, lcgEdges)
        for scc in SCC:
            if len(scc) > 1:
                cycle = True
                lcgEdges = breakCycle(lcgEdges, scc, startNode, actionsByHitter, actions)
                break
    return lcgEdges
# def deleteExcessive
