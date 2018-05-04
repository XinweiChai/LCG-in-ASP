from pyasp.asp import Gringo4Clasp
from reconstruct import *
from factGenerator import generate
from itertools import product, permutations
import copy


def heuristics(k, lcgEdges, startNode, initialState):
    for i in range(1, k + 2):
        newlcgEdges = random_reconstruct(lcgEdges, startNode)
        res, x = ASP_solve(newlcgEdges, initialState, i)
        if res:
            return res, i
        #elif x == 0:
        #    return False, 1
    return False, k


def ASP_solve(lcgEdges, initialState, iteration):
    if not lcgEdges:
        return False, 0
    generate(initialState, lcgEdges)
    goptions = ''
    soptions = '1'
    solver = Gringo4Clasp(gringo_options=goptions, clasp_options=soptions)
    encoding = 'nested.lp'
    facts = 'fact.lp'
    result = solver.run([encoding, facts], collapseTerms=True, collapseAtoms=False)
    for s in result:
        for a in s:
            if a.pred() == 'reachable':
                return True, iteration
    return False, iteration


def exhaustive_run(orGates, orGatesItems, lcgEdges, startNode, initialState):
    if not orGates:
        return ASP_solve(lcgEdges, initialState, 0)
    for i in product(*orGatesItems):
        lcgEdgesCopy = copy.copy(lcgEdges)
        for j in range(len(orGates)):
            lcgEdgesCopy[orGates[j]] = [i[j]]
        lcgEdgesCopy = prune(lcgEdgesCopy, startNode)
        res, x = ASP_solve(lcgEdgesCopy, initialState, 0)
        if res:
            return True, 0
    return False, 0


def prune(lcgEdges, startNode):
    modif = True
    while modif:
        modif = False
        temp = list(lcgEdges.keys())
        for i in temp:
            if i != startNode:
                mark = False
                for j in lcgEdges.values():
                    if i in j:
                        mark = True
                        break
                if not mark:
                    modif = True
                    del lcgEdges[i]
    return lcgEdges


def heuristics_perm_reach(k, lcgNodes, lcgEdges, startNode, initialState):
    if startNode in initialState:
        return True
    for i in range(k):
        newlcgEdges = random_reconstruct(lcgEdges, startNode)
        if not newlcgEdges:
            return False, 1
        if and_gate(lcgNodes, newlcgEdges, startNode, initialState):
            return True, i + 1
    return False, k


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
            flag_leaf = False
            for j in permutations(i[0]):
                flag = True
                temp_state = initialState
                for k in j:
                    [boo, state, sequence] = simple_branch(k, temp_state, lcgEdges)
                    if not boo:
                        flag = False
                        break
                    else:
                        temp_state = state
                if flag:
                    flag_leaf = True
                    initialState = temp_state
                    initialState[i[1]] = i[3]
                    break
            if not flag_leaf:
                return False
        for i in leaves:
            andGatesDict.pop(i)
            for j in andGatesDict:
                if i in andGatesDict[j]:
                    andGatesDict[j].remove(i)
        leaves = [i for i in andGatesDict if not andGatesDict[i]]
    return True


def simple_branch(target, state, lcgEdges):
    if state[target[0]] == target[1]:
        return True, state, None
    temp = lcgEdges[target]
    if not temp:
        return False, None, None
    temp = temp[0]
    sequence = [temp]
    count = 0
    while lcgEdges[temp]:
        count = count + 1
        temp = lcgEdges[temp][0]
        if count % 2 == 0:
            sequence.append(temp)
    list.reverse(sequence)
    for i in sequence:
        for j in i[0]:
            if state[j[0]] != j[1]:
                return False, None, None
            else:
                state[i[1]] = i[3]
    return True, state, sequence
