from readBAN import *
from SLCG import *
from cycle import *
from precodition import *
from heuristics import *
from batchTest import *
import timeit
#import argparse
start = timeit.default_timer()
#batch('data_tcr','tcrsig94.an')
#batch('data_egfr','egfr104.an')
batch('data_phage','testPhage')

stop = timeit.default_timer()

print(stop - start)
#iteration=500
#parser = argparse.ArgumentParser()
#parser.add_argument("fn")
#parser.add_argument("init")
#args=parser.parse_args()
#[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN(args.fn)
#startNode=tuple(re.split('=',args.init))
#[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('tcrsig94.an')

#[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('OrTest.lp')
#[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('LCG5')
#[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('loopTest.lp')
#[lcgNodes, lcgEdges] = SLCG(initialState, actions, startNode)
#lcgEdges=cycle(lcgNodes,lcgEdges, startNode, actionsByHitter, actions)
#lcgEdges = precondition(lcgEdges, actionsByHitter,initialState)
#heuristics(iteration,lcgEdges,startNode,initialState,lcgNodes)
