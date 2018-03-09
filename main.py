#from __future__ import print_function
from pyasp.asp import *
from SCC import strongly_connected_components_path
#input
#tentatives on translation from Matlab to Python
#stateNodeArray adjMatrix solNodeArray
#initialState actions startNode
f=open('data/LCG1','r')
for line in f.readlines():
    line.split(" ")
    #print(line)

sccResult=[]
#for scc in strongly_connected_components_path(vertices, edges):
#    sccResult.append(scc)
#preconditioning
#adjacent list perhaps faster
#while SCC is valid, break cycle

#begin for
#from root node, choose arbitrarily

#a possible alternative for ASP part is to enumerate all the possible combinations of OR gates
#write fact file

goptions = ''
soptions = '1'
solver   = Gringo4Clasp(gringo_options=goptions, clasp_options=soptions)
encoding = 'nestedTest.lp'
facts    = 'LCGexample5.pl'
result   = solver.run([encoding, facts], collapseTerms=True, collapseAtoms=False)
for s in result : 
  for a in s :
    args= ",".join(a.args())
    print(a.pred(), '(',args, ')', sep='', end=' ')
  print()
#end for
