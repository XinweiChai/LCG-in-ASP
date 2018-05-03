from readBAN import *
from SLCG import *
from cycle import *
from precodition import *
from heuristics import *
from readBAN import *
from batchTest import *
from generateModel import *
from compareFile import *
from timeit import default_timer

size = 5
num_tran = size*7
models = 20
iteration = 50
# x=generate_random_AN(size, num_tran)
# writeFile(x,'testmodel',size)
#generateFiles(models, size, num_tran)
# import argparse
start = default_timer()
# batch('data_tcr','tcrsig94.an')
# batch('data_egfr','egfr104.an')
# batch('','testPhage.an')
#test_models(101, 102)
print(batch_iteration_test(0,100,'data//inputFile','model_'+str(size)+'//model'))
#one_run(500, 'model_5//model10', ['n1','n2','n3','n4','n5'], [1,1,0,0,0], ('n5','1'))
print(count_inconclusive('model_5//model', '.out', 100))
# print(iterationMarker('data_tcr','tcrsig94.an'))
# print(iterationMarker('data_egfr','egfr104.an'))
# print(iterationMarker('data_phage','testPhage.an'))
# print(iteration_test('data_orTest', 'orTest.an'))
stop = default_timer()

print(stop - start)
# iteration=500
# parser = argparse.ArgumentParser()
# parser.add_argument("fn")
# parser.add_argument("init")
# args=parser.parse_args()
# [dictionary,actions, actionsByHitter, initialState, startNode]=readBAN(args.fn)
# startNode=tuple(re.split('=',args.init))
# [dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('tcrsig94.an')

# [dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('OrTest.lp')
# [dictionary,actions, actionsByHitter, initialState, startNode]=readBAN('LCG5')
# [dictionary,actions, actionsByHitter, initialState, startNode]=read_BAN('model70')
# startNode=('n3','1')
# [lcgNodes, lcgEdges] = SLCG(initialState, actions, startNode)
# lcgEdges=cycle(lcgNodes,lcgEdges, startNode, actionsByHitter, actions)
# lcgEdges = precondition(lcgEdges, actionsByHitter,initialState)
# print(heuristics_perm_reach(iteration,lcgEdges,startNode,initialState,lcgNodes))
