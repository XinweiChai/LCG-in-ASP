from readBAN import *
from SLCG import *
from cycle import *
from precodition import *
from heuristics import *
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("fn")
parser.add_argument("init")
args=parser.parse_args()
[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN(args.fn)
startNode=tuple(re.split('=',args.init))
#[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('tcrsig94.an')
#[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('OrTest.lp')
#[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('LCG5')
#[dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('loopTest.lp')
[lcgNodes, lcgEdges] = SLCG(initialState, actions, startNode)
lcgEdges=cycle(lcgNodes,lcgEdges, startNode, actionsByHitter, actions)
lcgEdges = precondition(lcgEdges, actionsByHitter,initialState)
iteration=500
heuristics(iteration,lcgEdges,startNode,initialState,lcgNodes)