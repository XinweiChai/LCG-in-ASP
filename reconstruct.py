import random
def reconstruct(lcg,startNode)
    toVisit = startNode
    while toVisit
        temp = []
        for i in toVisit:
            if i in lcg:
                if len(lcg[i]) > 1:
                   toConnect = lcg[i][random.randint(0,len(lcg[i]))]
                   lcg[i] = toConnect
    return lcg
