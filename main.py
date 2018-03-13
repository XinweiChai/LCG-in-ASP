#from __future__ import print_function
from pyasp.asp import *
from SCC import strongly_connected_components_path
#input
#translation from Matlab to Python
[dictionary,actions, actionsByHitter, initialState, startState]=readBAN('data/LCG1','r')

[lcg , lcgNodes, lcgEdges] = SLCG(initialState, actions, startNode);
SCC = strongly_connected_components_path(lcgNodes, lcgEdges)
while len(SCC)!=len(lcgNodes):
    lcgEdges=breakCycle(lcgEdges, SCC,startNode, actionsByHitter, actions)
    SCC = strongly_connected_components_path(lcgNodes, lcgEdges)
lceEdges = precondition(lcgEdges, initialState)
reachable=0;
for i=1:500
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

