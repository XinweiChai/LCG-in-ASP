from pyasp.asp import *
import re
f = open("output","w")
for i in range(3):
  string='VAR '+chr(ord('a')+i)+' 0 1'
  print(string, file = f)
print(file=f)
goptions = ''
soptions = '1'
solver   = Gringo4Clasp(gringo_options=goptions, clasp_options=soptions)
encoding = 'stateGenerator.lp'
facts    = ''
result   = solver.run([encoding, facts], collapseTerms=True, collapseAtoms=False)
for s in result : 
  for a in s :
    args= ",".join(a.args())
    trans = re.sub('state|\(|\)|\,','',args)
    trans = 'a='+ trans[0]+' b='+trans[1]+' c='+trans[2]+' : '+'a='+trans[3]+' b='+trans[4]+' c='+trans[5]
    print(trans, file = f)
  print(file=f)
