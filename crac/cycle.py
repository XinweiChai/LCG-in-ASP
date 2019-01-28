from SCC import strongly_connected_components_path


def break_cycle(lcg_edges, scc, start_node, actions_by_hitter, actions):
    if start_node in scc:
        lcg_edges = delete_element(start_node, scc, lcg_edges, actions, actions_by_hitter)
    else:
        for i in scc:
            if len(i) == 2:  # state node
                for j in actions_by_hitter[i]:
                    for k in (j[1], j[3]):
                        if k not in scc:
                            lcg_edges = delete_element(i, scc, lcg_edges, actions, actions_by_hitter)
                            return lcg_edges
    return lcg_edges


def delete_element(element, scc, lcg_edges, actions, actions_by_hitter):
    for i in scc:
        if i in actions_by_hitter[element]:
            lcg_edges[i] = []
            actions[(i[1], i[3])].remove(i)
    return lcg_edges


def cycle(lcg_nodes, lcg_edges, start_node, actions_by_hitter, actions):
    has_cycle = True
    while has_cycle:
        has_cycle = False
        SCC = strongly_connected_components_path(lcg_nodes, lcg_edges)
        for scc in SCC:
            if len(scc) > 1:
                has_cycle = True
                lcg_edges = break_cycle(lcg_edges, scc, start_node, actions_by_hitter, actions)
                break
    return lcg_edges


def cycle2(lcg_nodes, lcg_edges, start_node, actions_by_hitter, actions):
    has_cycle = True
    while has_cycle:
        has_cycle = False
        SCC = strongly_connected_components_path(lcg_nodes, lcg_edges)
        single_incoming = []
        for i in SCC:
            count_incoming = 0
            for j in i:
                contain = False
                for k in actions_by_hitter[j]:
                    for m in k:
                        if m not in SCC:
                            contain = True
                if contain:
                    count_incoming = count_incoming + 1
            if count_incoming <= 1:
                single_incoming.append(i)
        for scc in single_incoming:
            if len(scc) > 1:
                has_cycle = True
                lcg_edges = break_cycle(lcg_edges, scc, start_node, actions_by_hitter, actions)
                break
    return lcg_edges
