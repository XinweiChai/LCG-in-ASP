def precondition(lcgEdges, initialState)
    for i,j in lcgEdges.items():
        if j not in lcgEdges.keys() and j not in initialState:
            lcgEdges.pop(i)
            precondition(lcgEdges,initialState)
    return lcgEdges
