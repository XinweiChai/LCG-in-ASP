def SLCG(initialState, actions, actionsByHitter,startNode):
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
        LS = LS|set([i])
        ls.pop(0)
        #if i[1] == initialState[i[0]]:
        if i in initialState:
            continue
        else:
            act = [actions[value] for value in targets if value == i]
            lcgNodes+=act
            for j in act:
                solNode = [i,j]
                lcgEdges[i]=j
                lsToAct.append(solNode)
                for k in j[0]:
                    lcgEdges[j]=k
                    actToLs.append((j,k))
                    ls.append(k)
    lcg=[actToLs, lsToAct]
    return lcg , lcgNodes, lcgEdges#, solNodeArray
