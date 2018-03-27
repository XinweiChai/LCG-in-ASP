def SLCG(initialState, actions, startNode):
    actToLs=[]
    lsToAct=[]
    lcgNodes=[]
    lcgEdges={}
    #processdictionary
    targets = []
    for i in actions.values():
        targets.append((i[1],i[3]))
    ls = [startNode]# current node
    LS = set([])#LS = set([startNode]) # traversed nodes 
    while ls:
        i=ls[0]
        if i in LS: #and [i] != LS:
            ls.pop(0)
            continue
        lcgNodes.append(i)
        LS = LS | {i}
        ls.pop(0)
        #if i[1] == initialState[i[0]]:
        if i in initialState:
            continue
        else:
            act = [actions[value] for value in targets if value == i]
            lcgEdges[i]=act
            lcgNodes+=act
            for j in act:
                solNode = [i,j]
                lsToAct.append(solNode)
                lcgEdges[j] = list(j[0])
                for k in j[0]:
                    actToLs.append((j,k))
                    ls.append(k)
    for i in lcgNodes:
        if i not in lcgEdges:
            lcgEdges[i]=[]
    lcg=[actToLs, lsToAct]
    return lcg , lcgNodes, lcgEdges#, solNodeArray
