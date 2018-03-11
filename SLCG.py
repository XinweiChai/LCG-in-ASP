def SLCG(initialState, actions, startNode):
    actToLs=[]
    lsToAct=[]
    lcgNodes=[]
    lcgEdges={}
    #processdictionary
    targets = []
    dictionary = 
    for i in actions.values():
        targets.append([i[1],i[3]]) 
    ls = [startNode]# current node
    LS = set([])#LS = set([startNode]) # traversed nodes 
    while ls
        for i in ls:
            if i in LS #and [i] != LS:
                ls.pop()
                continue;
            lcgNodes.append(i)
            LS = LS|set([i])
            ls.pop()
            #if i[1] == initialState[i[0]]:
            if i in initialState
                continue
            else
                act = [index for index, value in enumerate(targets) if value == i]
                lcgNodes+=act
                for j in act:
                    solNode = [i,j]
                    lcgEdges[i]=j
                    lsToAct.append(solNode)
                    for k in actions[j]:
                        lcgEdges[j]=k
                        actToLs.append([j,k])
                        LS.append(k)
    lcg=[actToLs, lsToAct]
    return stateNodeArray, lcg , lcgNodes, lcgEdges#, solNodeArray
