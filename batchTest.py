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
            output_file(500, fo, fnetwork, input, i, j)
    fo.close()


def output_file(iterations, fout, fnetwork, input_instance, i, j):
    [boo, iterations] = one_run(iterations, fnetwork, input_instance, i, (j, '1'))
    fout.writelines("# " + j + "=1\n")
    if boo:
        fout.writelines("True\n")
    elif iterations == 0 or iterations == 1:
        fout.writelines("False\n")
    else:
        fout.writelines("Inconclusive\n")
    return boo, iterations


def iteration_test(fn, fnetwork):  # count the average and max iteration
    fo = open(fnetwork + '.out', 'w')
    if fn:
        f = open(fn, 'r')
        input = re.split(' ', f.readline().replace("\n", ""))
        output = re.split(' ', f.readline().replace("\n", ""))
        f.close()
    else:
        [dictionary, actions, actionsByHitter, initialState, startNode] = read_BAN(fnetwork)
        input = dictionary
        output = dictionary
    trial = 1
    totalTrial = 0
    reachCount = 0
    maxCount = 0
    inc = 0
    for k in range(trial):
        for i in product([0, 1], repeat=len(input)):
            fo.write("--- ")
            for k in range(len(i) - 1):
                fo.write(input[k] + "=" + str(i[k]) + ", ")
            fo.write(input[-1] + "=" + str(i[-1]) + "\n")
            # fo.writelines(str(i)+"\n")
            for j in output:
                [res, iter] = output_file(500, fo, fnetwork, input, i, j)
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


def one_run(iterations, fnetwork, input, changeState, start):
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
    orGates = []
    orGatesItems = []
    for i in lcgEdges:
        if len(i) == 2 and len(lcgEdges[i]) > 1:
            orGates.append(i)
            orGatesItems.append(lcgEdges[i])
    return heuristics_perm_reach(iterations, lcgNodes, lcgEdges, startNode, initialState)
    #return heuristics(iterations, lcgEdges, startNode, initialState)
    #print(initialState)
    #print(startNode)
    #if len(orGates) > 10:
    #    return heuristics(len(orGates)*5, lcgEdges, startNode, initialState)
    #else:
    #    return exhaustive_run(orGates, orGatesItems, lcgEdges, startNode, initialState)
