import numpy as np
import copy


def discrete(ts):  # to Boolean
    discrete_ts = np.zeros((len(ts), len(ts[0])))
    mu = ts.mean(1)
    for i in range(len(ts)):
        for j in range(len(ts[i])):
            if ts[i][j] >= mu[i]:
                discrete_ts[i][j] = 1
            # else:
            #    discrete_ts[i][j] = 0
    return discrete_ts


def change_rate(ts):
    before = copy.deepcopy(ts)
    after = copy.deepcopy(ts)
    num_var = len(ts)
    period = len(ts[0])
    before = np.delete(before, -1, 1)
    after = np.delete(after, 0, 1)
    for i in range(num_var):
        for j in range(period - 1):
            after[i][j] = after[i][j] - before[i][j]
    return after


def regroup(ts_cut, cr):
    reg = np.zeros((len(ts_cut), len(ts_cut), len(cr[0])))
    for k in range(len(reg)):
        for i in range(len(reg[0])):
            if i == k:
                reg[k][i] = cr[i]
            else:
                reg[k][i] = ts_cut[i]
    return reg
