from pyasp.asp import *
from reconstruct import *
from factGenerator import *
def heuristic(k,lcgEdges,startNode,initialState,lcgNodes):
    reachable=0
    for i in range(k):
        lcgEdges = reconstruct(lcgEdges,startNode)
        generate(initialState, lcgNodes, lcgEdges)
        goptions = ''
        soptions = '1'
        solver   = Gringo4Clasp(gringo_options=goptions, clasp_options=soptions)
        encoding = 'nested.pl'
        facts    = 'fact.lp'
        result   = solver.run([encoding, facts], collapseTerms=True, collapseAtoms=False)
        for s in result:
            for a in s:
                if a.pred()=='reachable':
                    print('reachable')
                    return 1
    print('unreachable')
    return 0
