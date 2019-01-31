import re


def rule_parser(fn):  # in form of "c(0,T)::5/10 :- b(1,T-1)." --> ['c','0','b','1']
    f = open(fn, 'r')
    data = []
    for i in f.read().splitlines():
        temp = re.sub("::|,T(-1)*|%|\d+\/\d+|\.|\)|\s", '', i)
        temp = re.split(":-|,|\(", temp)
        # print(temp)s
        data.append(temp)
    f.close
    return data


def transition_parser(fn):  # parse file 'output' time-series data
    f = open(fn, 'r')
    data = []
    var_count = 0
    for i in f.readlines():
        if i == '\n':
            continue
        if re.match("VAR", i):
            var_count = var_count + 1
            continue
        temp = re.sub("\n", '', i)
        temp = re.split(" *: *", temp)
        for j in range(len(temp)):
            temp[j] = re.split(' ', temp[j])
            for k in range(len(temp[j])):
                temp[j][k] = re.split('=', temp[j][k])
        data.append(temp)
    f.close
    return data


# we don't need reachability parser for now as it can be generated by ASPReach

def reachability_parser(fn):  # (c,1,state(1,1,1))/unreachable
    f = open(fn, 'r')
    data = []
    for i in f.readlines():
        if i == '\n':
            continue
        temp = re.sub("reachable|state|\(|\)|\n", '', i)
        temp = re.split(" ", temp)
        for j in temp:
            temp2 = re.split(",", j)
            data.append(temp2)
    f.close
    return data


x = transition_parser("output")
y = rule_parser("rules")
z = reachability_parser("result")
