def precondition(lcg, initialState)
    for i,j in lcg.items():
        if j not in lcg.keys() and j not in initialState:
            lcg.pop(i)
            precondition(lcg,initialState)
    return lcg
