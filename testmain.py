from readBAN import *
from SLCG import *
from cycle import *
from precodition import *
from heuristics import *

[dictionary, actions, actionsByHitter, initialState, startNode] = read_BAN('tcrsig94.an')
# [dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('OrTest.lp')
# [dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('LCG5')
# [dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('loopTest.lp')
[lcgNodes, lcgEdges] = SLCG(initialState, actions, startNode)
lcgEdges = cycle(lcgNodes, lcgEdges, startNode, actionsByHitter, actions)
lcgEdges = precondition(lcgEdges, actionsByHitter, initialState)
iteration = 500
heuristics(iteration, lcgEdges, startNode, initialState)
