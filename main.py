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

sizes = [30,40,50,60,70,80,1000]
size = 20
times=[1,2,3,4,5,6,7]
num_tran_var = size*times
num_tran=size
models = 20
iteration = 50
# x=generate_random_AN(size, num_tran)
# writeFile(x,'testmodel',size)
generateFiles(models, size, num_tran)
# import argparse
start = default_timer()
# batch('data_tcr','tcrsig94.an')
# batch('data_egfr','egfr104.an')
# batch('','testPhage.an')
#test_models(101, 102)
#for i in range(20):
#    print(str(i),compare_file('model_80//model'+str(i)+'.out','data//run-model'+str(i)+'.out'))
#print(batch_iteration_test(0,100,'data//inputFile','model_'+str(size)+'//model'))
#print(batch_iteration_test(0,100,'data//inputFile','model_'+str(size)+'_exhaustive//model'))
print(one_run('model_20//model18', ['n1','n2','n3','n4','n5'], [0,1,0,0,0], ('n4','1')))
#print(one_run('model_80//model18', ['n1','n2'], [0,0,0,0,0], ('n7','1')))
#f=open('count_result','a')
#for i in sizes:
#    begin=default_timer()
#    #print(batch_iteration_test(0, models, 'data//inputFile', 'model_' + str(i) + '//model'))
#    print(batch_iteration_test(0, models, 'data//inputFile', 'model_' + str(i) + '//model'))
#    #f.writelines(str(count_result('model_' + str(i) + '//model', '.out', models))+'\n')
#    end=default_timer()
#    print(end-begin)

#for i in times:
#    begin=default_timer()
#    generateFiles(models, size, size*i)
#    print(batch_iteration_test(0, models, 'data//inputFile', 'model_20//model'))
    #f.writelines(str(count_result('model_' + str(i) + '//model', '.out', models))+'\n')
#    end=default_timer()
#    print(end-begin)
#print(batch_iteration_test(0, models, 'data//inputFile', 'model_20//model'))
#f.writelines(str(count_result('model_' + str(size) + '//model', '.out', models))+'\n')
#f.writelines(str(count_result('data//run-model', '.out', models))+'\n')
#f.close
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
