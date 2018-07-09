def precondition(lcg_edges, actions_by_hitter, initial_state):
    mark = True
    while mark:
        mark = False
        for i in list(lcg_edges):
            if not lcg_edges[i] and i not in initial_state.items():  # and len(i) == 4:
                lcg_edges.pop(i)
                mark = True
                continue
            if len(i) == 4:
                for k in lcg_edges[i]:
                    if k not in lcg_edges:
                        mark = True
                        lcg_edges.pop(i)
                        break
            elif len(i) == 2 and i not in initial_state.items():
                for k in lcg_edges[i]:
                    if k not in lcg_edges:
                        lcg_edges[i].remove(k)
                        mark = True
                        break
        # if mark:
        #     lcg_edges.pop(i)
        #     for j in lcg_edges[i]:
        #         lcg_edges.pop(j)
        #         lcg_edges[(j[1],j[3])].remove(j)
        # lcg_edges=precondition(lcg_edges, actions_by_hitter,initial_state)
    return lcg_edges
