from partial_corr import *
from models import *
from tools import *


def random_test(num_var, period, up_threshold, down_threshold, noise):
    eq = generate_random_continuous_model(num_var)
    initial_state = np.ones(num_var)
    ts = evolve(initial_state, period, eq, noise)
    discrete_ts = discrete(ts)
    cr = change_rate(ts)
    ts_cut = np.delete(ts, -1, 1)
    # regroup
    reg = regroup(ts_cut, cr)
    partial_matrix = np.zeros((num_var, num_var))
    for i in range(len(reg)):
        partial_matrix[i] = partial_corr(reg[i].transpose())[i]
    above_threshold = []
    below_threshold = []
    for i in range(len(partial_matrix)):
        for j in range(len(partial_matrix[0])):
            if abs(partial_matrix[i][j]) > up_threshold and i != j:
                above_threshold.append((i, j))
            elif abs(partial_matrix[i][j]) < down_threshold and i != j:
                below_threshold.append((i, j))
    return eq, ts, discrete_ts, partial_matrix, above_threshold, below_threshold


def consistent_rate(eq, res_mat, threshold):
    false_positive = 0
    false_negative = 0
    positive = 0
    negative = 0
    for i in range(len(eq)):
        for j in range(len(eq[0])):
            if i != j:
                if abs(res_mat[i][j]) < threshold:
                    negative = negative + 1
                    if np.sign(eq[i][j]) != 0:
                        false_negative = false_negative + 1
                else:
                    positive = positive + 1
                    if np.sign(eq[i][j]) != np.sign(res_mat[i][j]):
                        false_positive = false_positive + 1
    if positive != 0:
        false_positive_rate = false_positive / positive
    else:
        false_positive_rate = 0
    if negative != 0:
        false_negative_rate = false_negative / negative
    else:
        false_negative_rate = 0
    return false_positive_rate, false_negative_rate


def consistent_rate2(eq, res_mat, threshold):
    correct = 0
    for i in range(len(eq)):
        for j in range(len(eq[0])):
            if i != j:
                if (res_mat[i][j] <= -threshold and eq[i][j] < 0) or \
                        (res_mat[i][j] >= threshold and eq[i][j] > 0) or \
                        (-threshold < res_mat[i][j] < threshold and eq[i][j] == 0):
                    correct = correct + 1
    return correct / len(eq) / (len(eq)-1)


