def precondition(lcgEdges, actionsByHitter,initialState):
    mark=True
    while mark:
        mark = False
        for i in list(lcgEdges):
            if not lcgEdges[i] and i not in initialState.items():# and len(i) == 4:
                lcgEdges.pop(i)
                mark=True
                continue
            if len(i)==4:
                for k in lcgEdges[i]:
                    if k not in lcgEdges:
                        mark=True
                        lcgEdges.pop(i)
                        break
            elif len(i)==2 and i not in initialState.items():
                for k in lcgEdges[i]:
                    if k not in lcgEdges:
                        lcgEdges[i].remove(k)
                        mark=True
                        break
           # if mark:
           #     lcgEdges.pop(i)
           #     for j in lcgEdges[i]:
           #         lcgEdges.pop(j)
           #         lcgEdges[(j[1],j[3])].remove(j)
                        #lcgEdges=precondition(lcgEdges, actionsByHitter,initialState)
    return lcgEdges
