from __future__ import print_function
from pyasp.asp import *
#input
f=open('path','r')
f.read()
#use a class to save all the parameters

#preconditioning
#while SCC is valid, break cycle

#begin for
#from root node, choose arbitrarily

#write fact file

goptions = ''
soptions = '1'
solver   = Gringo4Clasp(gringo_options=goptions, clasp_options=soptions)
encoding = 'nestedTest.lp'
facts    = 'LCGexample6.pl'
result   = solver.run([encoding, facts], collapseTerms=True, collapseAtoms=False)
for s in result : 
  for a in s :
    args= ",".join(a.args())
    print(a.pred(), '(',args, ')', sep='', end=' ')
  print()
#end for
