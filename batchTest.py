from readBAN import *
from SLCG import *
from cycle import *
from precodition import *
from heuristics import *
import itertools

def batch(fn,fnetwork):
    f=open(fn,'r')
    fo=open(fn+"_out",'w')
    input = re.split(' ', f.readline().replace("\n", ""))
    output = re.split(' ', f.readline().replace("\n", ""))
    for i in itertools.product([0, 1], repeat=len(input)):
        fo.write("--- ")
        for k in range(len(i)-1):
            fo.write(input[k]+"="+str(i[k])+", ")
        fo.write(input[-1]+"="+str(i[-1])+"\n")
        #fo.writelines(str(i)+"\n")
        for j in output:
            if one_run(500, fnetwork,input, i, (j,'1')):
                fo.writelines("# "+j+"=1\n")
                fo.writelines("True\n")
            else:
                fo.writelines("# "+j+"=1\n")
                fo.writelines("False\n")


def one_run(iteration,fnetwork,input, changeState, start):
    #parser = argparse.ArgumentParser()
    #parser.add_argument("fn")
    #parser.add_argument("init")
    #args=parser.parse_args()
    #[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN(args.fn)
    #startNode=tuple(re.split('=',args.init))
    #[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('tcrsig94.an')
    [dictionary,actions, actionsByHitter, initialState, startNode]=readBAN(fnetwork)
    for i in input:
        initialState[i]=str(changeState[input.index(i)])
    startNode = start

    #[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('OrTest.lp')
    #[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('LCG5')
    #[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('loopTest.lp')
    [lcgNodes, lcgEdges] = SLCG(initialState, actions, startNode)
    lcgEdges=cycle(lcgNodes,lcgEdges, startNode, actionsByHitter, actions)
    lcgEdges = precondition(lcgEdges, actionsByHitter,initialState)
    return heuristics(iteration,lcgEdges,startNode,initialState,lcgNodes)
