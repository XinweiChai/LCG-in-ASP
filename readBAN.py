import re


def read_BAN(path):
    readProc = 0
    process = []
    actions = {}
    actionsByHitter = {}
    initialState = {}
    startState = []
    f = open('data//'+path, 'r')
    for line in f.readlines():
        line = line.replace("\n", "")
        if 'goal' in line:
            words = re.split(",*\s|\(\*|\*\)", line)
            startState = words[words.index('goal') + 1]
            startState = re.split("[_=]", startState)
            startState = tuple(startState)
        else:
            words = re.split("\s*and\s*|,\s*|\s+", line)
            if len(words) <= 1:
                continue
            elif (len(words) > 3) and (not readProc):
                readProc = 1
            if not readProc:
                process.append(words[0])
                actions[(words[0], '0')] = []
                actions[(words[0], '1')] = []
                actionsByHitter[(words[0], '0')] = []
                actionsByHitter[(words[0], '1')] = []
                initialState[words[0]] = '0'
                continue
            else:
                if words[0] != 'initial_state':
                    act = [[]]
                    act.append(words[0])
                    act.append(words[1])
                    act.append(words[3])
                    for i in range(len(words) - 5):
                        temp = re.split("=", words[i + 5])  # last elements
                        act[0].append((temp[0], temp[1],))
                    act[0] = tuple(act[0])
                    act = tuple(act)
                    actions[(words[0], words[3])].append(act)
                    for i in act[0]:
                        actionsByHitter[i].append(act)
                else:
                    for i in words[1:]:
                        temp = re.split("=", i)
                        initialState[temp[0]] = temp[1]
    return process, actions, actionsByHitter, initialState, startState
