from random import randint


def random_reconstruct(lcgEdges, startNode):
    newlcgEdges = {}
    toVisit = [startNode]
    if startNode not in lcgEdges:
        return None
    while toVisit:
        for i in toVisit:
            if len(lcgEdges[i]) >= 1:
                choose = lcgEdges[i][randint(0, len(lcgEdges[i]) - 1)]
                newlcgEdges[i] = [choose]
                newlcgEdges[choose] = list(choose[0])
                toVisit.extend(choose[0])
            else:
                newlcgEdges[i] = []
            toVisit.remove(i)
    return newlcgEdges
