#from __future__ import print_function
from pyasp.asp import *
from readBAN import *
from SLCG import *
from SCC import strongly_connected_components_path
#input
#translation from Matlab to Python
[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('LCG1')

[lcg , lcgNodes, lcgEdges] = SLCG(initialState, actions, actionsByHitter, startNode);
SCC = strongly_connected_components_path(lcgNodes, lcgEdges)
vertices = [1, 2, 3, 4, 5, 6]
edges = {1: [2, 3], 2: [3, 4], 3: [], 4: [3, 5], 5: [2, 6], 6: [3, 4]}
SCCtest = strongly_connected_components_path(vertices,edges)
length=len(list(SCC))
while len(SCC)!=len(lcgNodes):
    lcgEdges=breakCycle(lcgEdges, SCC,startNode, actionsByHitter, actions)
    SCC = strongly_connected_components_path(lcgNodes, lcgEdges)
lceEdges = precondition(lcgEdges, initialState)
reachable=0;
for i in range(500):
    lcgEdges = reconstruct(lcgEdges,startNode)
    goptions = ''
    soptions = '1'
    solver   = Gringo4Clasp(gringo_options=goptions, clasp_options=soptions)
    encoding = 'nestedTest.lp'
    facts    = 'LCGexample5.pl'
    result   = solver.run([encoding, facts], collapseTerms=True, collapseAtoms=False)
    for s in result : 
        for a in s :
            reachable=1
            break
        if reachable:
            break
    if reachable:
        break
if reachable:
    print('reachable')
else:
    print('unreachable');

