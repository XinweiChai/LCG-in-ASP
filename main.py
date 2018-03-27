from readBAN import *
from SLCG import *
from breakCycle import *
from precodition import *
from heuristic import *
[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('LCG5')

[lcg , lcgNodes, lcgEdges] = SLCG(initialState, actions, startNode)
lcgEdges=cycle(lcgNodes, lcgEdges, startNode, actionsByHitter, actions)
lcgEdges = precondition(lcgEdges, initialState)
heuristic(500,lcgEdges,startNode,initialState,lcgNodes)