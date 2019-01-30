from pyasp.asp import *
import re
import random
import itertools


def write_literal(f, var_num):
    for j in range(var_num):
        if j == 0:
            f.write("V" + str(j))
        else:
            f.write(", V" + str(j))


def asp_generator(var_num, trans_num):
    f = open("fact.lp", "w")
    for i in itertools.product([0, 1], repeat=var_num):
        f.write("state" + str(i) + ".\n")
    f.close()
    f = open('stateGenerator.lp', "w")
    for i in range(var_num):
        f.write("{trans(")
        f.write("state(")
        write_literal(f, var_num)
        f.write("), ")
        f.write("state(")
        for j in range(var_num):
            if j == 0:
                f.write("V")
            else:
                f.write(",V")
            if i == j:
                f.write(str(j) + "X")
            else:
                f.write(str(j))
        f.write("))} :- ")
        f.write("state(")
        write_literal(f, var_num)
        f.write("), ")
        f.write("state(")
        for j in range(var_num):
            if j == 0:
                f.write("V")
            else:
                f.write(", V")
            if i == j:
                f.write(str(j) + "X")
            else:
                f.write(str(j))
        f.write("), ")
        f.write("V" + str(i) + "!=V" + str(i) + "X.\n")

    f.write(":- {trans(state(")
    write_literal(f, var_num)
    f.write("), _)}0, state(")
    write_literal(f, var_num)
    f.write(").\n")

    f.write(":- {trans(state(")
    write_literal(f, var_num)
    f.write("), state(")
    for j in range(var_num):
        if j == 0:
            f.write("V" + str(j) + "X")
        else:
            f.write(", V" + str(j) + "X")
    f.write(")) : trans(state(")
    write_literal(f, var_num)
    f.write("), state(")
    for j in range(var_num):
        if j == 0:
            f.write("V" + str(j) + "X")
        else:
            f.write(", V" + str(j) + "X")
    f.write("))}" + str(trans_num) + ".\n")
    f.write("#show trans/2.")
    f.close()
    return 0


var_num = 4
trans_num = 17
asp_generator(var_num, trans_num)
f = open("output", "w")
for i in range(var_num):
    # string = 'VAR ' + chr(ord('a') + i) + ' 0 1'
    string = 'VAR ' + "V" + str(i) + ' 0 1'
    print(string, file=f)
print(file=f)
goptions = ''
soptions = '50'
solver = Gringo4Clasp(gringo_options=goptions, clasp_options=soptions)
encoding = 'stateGenerator.lp'
facts = 'fact.lp'
result = solver.run([encoding, facts], collapseTerms=True, collapseAtoms=False)
if result:
    x = random.randint(0, len(result) - 1)
    for a in result[x]:
        args = ",".join(a.args())
        trans = re.sub('state|\(|\)|\,', '', args)
        temp = ''
        for i in range(var_num):
            temp = temp + 'V' + str(i) + "=" + trans[i] + ' '
        temp = temp + ': '
        for i in range(var_num):
            temp = temp + 'V' + str(i) + "=" + trans[i + var_num] + ' '
        trans = 'a=' + trans[0] + ' b=' + trans[1] + ' c=' + trans[2] + ' : ' + 'a=' + trans[3] + ' b=' + trans[
            4] + ' c=' + trans[5]
        print(temp, file=f)
# for s in result : 
#   for a in s :
#     args= ",".join(a.args())
#     trans = re.sub('state|\(|\)|\,','',args)
#     trans = 'a='+ trans[0]+' b='+trans[1]+' c='+trans[2]+' : '+'a='+trans[3]+' b='+trans[4]+' c='+trans[5]
#     print(trans, file = f)
#   print(file=f)
