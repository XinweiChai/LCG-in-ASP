from pyasp.asp import *
from reconstruct import *
from factGenerator import *
def heuristics(k,lcgEdges,startNode,initialState,lcgNodes):
    if startNode in initialState:
        #print('reachable')
        return True
    for i in range(k):
        newlcgEdges = reconstruct(lcgEdges,startNode)
        if not newlcgEdges:
            #print('unreachable')
            return False,1
        generate(initialState,  newlcgEdges)
        goptions = ''
        soptions = '1'
        solver   = Gringo4Clasp(gringo_options=goptions, clasp_options=soptions)
        encoding = 'nested.lp'
        facts    = 'fact.lp'
        result   = solver.run([encoding, facts], collapseTerms=True, collapseAtoms=False)
        for s in result:
            for a in s:
                if a.pred()=='reachable':
                    #print('reachable')
                    return True,i+1
    #print('unreachable')
    return False,k