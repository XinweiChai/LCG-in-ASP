from batchTest import *


def pre_check(fnetwork, reach, unreach):
    reach1 = []
    unreach1 = []
    for i in reach:
        res, x = one_run(fnetwork, i[0], i[1], i[2])
        if not res:
            unreach1.append(i)
    for i in unreach:
        res, x = one_run(fnetwork, i[0], i[1], i[2])
        if res:
            reach1.append(i)
    return reach1, unreach1


def specilization(an, reach, unreach, unreach1):
    l = {}
    for i in unreach1:
        l[i] = []
    for i in reach + unreach:
        for j in l:
            if i[2] in lcg(j):
                l[i].append(j)
    size_count = 0
    while l:
        for i in l:
            if len(l[i]) == size_count:
                specialize()
        size_count = size_count + 1
    return an


def generalization(an, reach, unreach, unreach1):
    return an
