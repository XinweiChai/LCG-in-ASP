from SCC import strongly_connected_components_path


def break_cycle(lcg_edges, scc, start_node, actions_by_hitter, actions):
    if start_node in scc:
        lcg_edges = delete_element(start_node, scc, lcg_edges, actions, actions_by_hitter)
    else:
        for i in scc:
            if len(i) == 2:
                for j in actions_by_hitter[i]:
                    # for k in j[0]:
                    for k in (j[1], j[3]):
                        if k not in scc:
                            lcg_edges = delete_element(i, scc, lcg_edges, actions, actions_by_hitter)
                            return lcg_edges
    return lcg_edges


def delete_element(element, scc, lcg_edges, actions, actions_by_hitter):
    for i in scc:
        if i in actions_by_hitter[element]:
            # lcg_edges[i].remove(element)
            lcg_edges[i] = []
            actions[(i[1], i[3])].remove(i)
            # for j in scc:
            #    if len(j)==2:
            #        if i in actions[j]:
            #            lcg_edges[j].remove(i)

    # lcg_edges[actions_by_hitter[element]] = []  # delete the link of preceding action->element
    # lcg_edges[(
    # actions[element][1], actions[element][3])] = []  # delete the link of pred of preceding action -> preceding action
    return lcg_edges


def cycle(lcg_nodes, lcg_edges, start_node, actions_by_hitter, actions):
    cycle = True
    while cycle:
        cycle = False
        SCC = strongly_connected_components_path(lcg_nodes, lcg_edges)
        for scc in SCC:
            if len(scc) > 1:
                cycle = True
                lcg_edges = break_cycle(lcg_edges, scc, start_node, actions_by_hitter, actions)
                break
    return lcg_edges
# def deleteExcessive
