from readBAN import *
from SLCG import *
from cycle import *
from precodition import *
from heuristics import *
from itertools import product


def batch(fn, fnetwork):  # comparison with Pint and PermReach
    fo = open('output//' + fnetwork + "_out", 'w')
    if fn:
        f = open('data//' + fn, 'r')
        input = re.split(' ', f.readline().replace("\n", ""))
        output = re.split(' ', f.readline().replace("\n", ""))
        f.close()
    else:
        [dictionary, actions, actionsByHitter, initialState, startNode] = read_BAN(fnetwork)
        input = dictionary
        output = dictionary
    for i in product([0, 1], repeat=len(input)):
        fo.write("--- ")
        for k in range(len(i) - 1):
            fo.write(input[k] + "=" + str(i[k]) + ", ")
        fo.write(input[-1] + "=" + str(i[-1]) + "\n")
        # fo.writelines(str(i)+"\n")
        for j in output:
            output_file(fo, fnetwork, input, i, j)
    fo.close()


def output_file(fout, fnetwork, input_instance, i, j):
    [boo, iterations] = one_run(fnetwork, input_instance, i, (j, '1'))
    fout.writelines("# " + j + "=1\n")
    if boo:
        fout.writelines("True\n")
    elif iterations == 0 or iterations == 1:
        fout.writelines("False\n")
    else:
        fout.writelines("Inconclusive\n")
    return boo, iterations


def iteration_test(f_network, f_out):  # count the average and max iteration
    fo = open(f_out + '.out', 'w')
    if f_network:
        f = open(f_network, 'r')
        input = re.split(' ', f.readline().replace("\n", ""))
        output = re.split(' ', f.readline().replace("\n", ""))
        f.close()
    else:  # if no input and output, input and output are set to universe by default
        [dictionary, actions, actionsByHitter, initialState, startNode] = read_BAN(f_out)
        input = dictionary
        output = dictionary
    totalTrial = 0
    reachCount = 0
    maxCount = 0
    inc = 0
    for i in product([0, 1], repeat=len(input)):
        fo.write("--- ")
        for k in range(len(i) - 1):
            fo.write(input[k] + "=" + str(i[k]) + ", ")
        fo.write(input[-1] + "=" + str(i[-1]) + "\n")
        # fo.writelines(str(i)+"\n")
        for j in output:
            [res, iter] = output_file(fo, f_out, input, i, j)
            if res:
                totalTrial = totalTrial + iter
                if iter > maxCount:
                    maxCount = iter
                reachCount = reachCount + 1
            else:
                if iter > 1:
                    inc = inc + 1
    if reachCount == 0:
        return 0, maxCount, inc
    else:
        average = totalTrial / reachCount
        return average, maxCount, inc


def test_models(begin, end):
    for i in range(begin, end):
        batch('', 'model' + str(i))


def batch_iteration_test(begin, end, fn, fnetwork):
    aver_of_average = 0
    max_of_max = 0
    aver_of_inc = 0
    for i in range(begin, end):
        print(i)
        average, maxCount, inc = iteration_test(fn, fnetwork + str(i))
        aver_of_average = aver_of_average + average
        aver_of_inc = aver_of_inc + inc
        if maxCount > max_of_max:
            max_of_max = maxCount
    return aver_of_average / (end - begin), max_of_max, aver_of_inc / (end - begin)


def one_run(fnetwork, input, changeState, start):
    [dictionary, actions, actionsByHitter, initialState, startNode] = read_BAN(fnetwork)
    for i in input:
        initialState[i] = str(changeState[input.index(i)])
    startNode = start
    # [dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('OrTest.lp')
    # [dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('LCG5')
    # [dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('loopTest.lp')
    [lcgNodes, lcgEdges] = SLCG(initialState, actions, startNode)
    lcgEdges = cycle(lcgNodes, lcgEdges, startNode, actionsByHitter, actions)
    lcgEdges = precondition(lcgEdges, actionsByHitter, initialState)
    lcgEdges = prune(lcgEdges, startNode)
    print(startNode)
    # print(initialState)
    if initialState[startNode[0]] == startNode[1]:
        return True, 0
    if startNode not in lcgEdges:
        return False, 0
    orGates = []
    orGatesItems = []
    for i in lcgEdges:
        if len(i) == 2 and len(lcgEdges[i]) > 1:
            orGates.append(i)
            orGatesItems.append(lcgEdges[i])
    # return exhaustive_reach(orGates, orGatesItems, lcgNodes, lcgEdges, startNode, initialState)
    if len(orGates) <= 10:
        return exhaustive_reach(orGates, orGatesItems, lcgNodes, lcgEdges, startNode, initialState)
    else:
        return heuristics_perm_reach(len(orGates) * 100 + 1, lcgNodes, lcgEdges, startNode, initialState)
    # return heuristics(len(orGates)*5+1, lcgEdges, startNode, initialState)
    # if len(orGates) > 9:
    #    return heuristics(len(orGates)*5+1, lcgEdges, startNode, initialState)
    # else:
    #    return exhaustive_run(orGates, orGatesItems, lcgEdges, startNode, initialState)
