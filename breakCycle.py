def breakCycle(lcgEdges, SCC,startNode, actionsByHitter, actions)
    for cycle in SCC:
        if len(cycle) == 1:
            continue
       #closest element to the desired state
        if startNode in cycle:
            transToDelete = actionsByHitter[startNode]
            nodesToDelete = []
            for i in transToDelete:
                nodesToDelete.append(actions[i])
            deleteElememt(nodesToDelete, lcgEdges,actions,actionsByHitter)

        else:
            for i in cycle:
                if len(actionsByHitter[i])>1: 
                    pred = actionByHitter[i]
                    for j in pred:
                        if (j[1],j[3]) in cycle:
                            deleteElememt((j[1],j[3]),lcgEdges,actions,actionsByHitter)
    return lcgEdges
def deleteElememt(element,lcgEdges,actions,actionsByHitter):
    lcgEdges[actionsByHitter[element]]=[]#delete the link of preceding action->element
    lcgEdges[(actions[element][1],actions[element][3])] = []#delete the link of pred of preceding action -> preceding action
    return lcgEdges


#def deleteExcessive
