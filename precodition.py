def precondition(lcg_edges, initial_state):
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
    return lcg_edges
