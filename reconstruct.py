import random
def reconstruct(lcgEdges,startNode):
    toVisit = startNode
    while toVisit:
        temp = []
        for i in toVisit:
            if i in lcgEdges:
                if len(lcgEdges[i]) > 1:
                   toConnect = lcgEdges[i][random.randint(0,len(lcgEdges[i]))]
                   lcgEdges[i] = toConnect
                temp.append(toConnect)
        toVisit=temp
    return lcgEdges
