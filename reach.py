# delete loops
# translate to asp
# solve

from pyasp.asp import *


def asp_exhaust_solve(fn_model):
    g_options = ''
    s_options = '1'
    solver = Gringo4Clasp(gringo_options=g_options, clasp_options=s_options)
    encoding = 'reachability.lp'
    facts = fn_model
    result = solver.run([encoding, facts], collapseTerms=True, collapseAtoms=False)
    print(result)
#    for s in result:
#        if Term('unreachable') in s:
#            return False, iteration
#        if Term('reachable') in s:
#            s.remove(Term('reachable'))
#            return True, iteration, s.to_list()
#    return False, iteration
