from pyasp.asp import Gringo4Clasp
from reconstruct import *
from factGenerator import generate
from itertools import permutations


def heuristics(k, lcgEdges, startNode, initialState):
    if startNode in initialState:
        # print('reachable')
        return True
    for i in range(k):
        newlcgEdges = reconstruct(lcgEdges, startNode)
        if not newlcgEdges:
            # print('unreachable')
            return False, 1
        generate(initialState, newlcgEdges)
        goptions = ''
        soptions = '1'
        solver = Gringo4Clasp(gringo_options=goptions, clasp_options=soptions)
        encoding = 'nested.lp'
        facts = 'fact.lp'
        result = solver.run([encoding, facts], collapseTerms=True, collapseAtoms=False)
        for s in result:
            for a in s:
                if a.pred() == 'reachable':
                    # print('reachable')
                    return True, i + 1
    # print('unreachable')
    return False, k


def heuristics_perm_reach(k, lcgNodes, lcgEdges, startNode, initialState):
    if startNode in initialState:
        return True
    for i in range(k):
        newlcgEdges = reconstruct(lcgEdges, startNode)
        if not newlcgEdges:
            return False
        if and_gate(lcgNodes, newlcgEdges, startNode, initialState):
            return True
    return False


def and_gate(lcgNodes, lcgEdges, startNode, initialState):
    andGates = [i for i in lcgEdges if len(lcgEdges[i]) > 1]
    andGatesDict = {}
    for i in andGates:
        andGatesDict[i] = []
        for j in lcgEdges[i]:
            temp = j
            while temp not in andGates and lcgEdges[temp]:
                temp = lcgEdges[temp][0]
            if temp in andGates:
                andGatesDict[i].append(temp)
    leaves = [i for i in andGatesDict if not andGatesDict[i]]
    if not andGatesDict:
        return True
    while leaves:
        for i in leaves:
            flag_leaf= False
            for j in permutations(i[0]):
                flag = True
                temp_state=initialState
                for k in j:
                    [boo, state, sequence]=simple_branch(k,temp_state,lcgEdges)
                    if not boo:
                        flag = False
                        break
                    else:
                        temp_state = state
                if flag:
                    flag_leaf = True
                    initialState = temp_state
                    break
            if not flag_leaf:
                return False
        for i in andGatesDict:
            for j in leaves:
                if j in andGatesDict[i]:
                    andGatesDict[i].remove(j)
        leaves = [i for i in andGatesDict if not andGatesDict[i]]
    return True

def simple_branch(target, state, lcgEdges):
    temp=target
    sequence=[temp]
    while lcgEdges[temp]:
        temp=lcgEdges[temp][0]
        if len(temp)==4:
            sequence.append(temp)
    list.reverse(sequence)
    for i in sequence:
        for j in i[0]:
            if j not in state:
                return False, None, None
    state[j[1]]=j[3]
    return True, state, sequence
