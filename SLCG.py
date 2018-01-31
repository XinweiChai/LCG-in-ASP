def SLCG(initialState, actions, startNode):
    lcg=[]
    #processdictionary
    targets = []
    for i in actions:
        targets.append([i[1],i[3]]) 
    ls = [startNode]
    LS = set([startNode])
    while ls
        for i in ls:
            if i in LS and [i] != LS:
                Ls.pop(0)
                continue;
            LS = LS|set([i])
            ls.pop()
            if i[1] == initialState[i[0]]:
                continue
            else
                nodei = stateNodeArray...
                act = [index for index, value in enumerate(targets) if value == i]
                for j in act:
                    solNode = [i,j]
                    lcg.append(solNode)
                    for k in actions[j]:
                        lcg.append([j,k])
                        LS.append(k)
    return stateNodeArray, lcg#, solNodeArray
