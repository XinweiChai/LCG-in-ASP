def precondition(lcgEdges, initialState):
    for i in lcgEdges.keys():
        if i not in initialState:
            mark=True
            for k in lcgEdges[i]:
                if k in lcgEdges:
                    mark=False
            if mark:
                lcgEdges.pop(i)
                precondition(lcgEdges, initialState)
    return lcgEdges
