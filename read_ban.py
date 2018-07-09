import re


def read_ban(path):
    read_proc = 0
    process = []
    actions = {}
    actions_by_hitter = {}
    initial_state = {}
    start_state = []
    f = open(path, 'r')
    for line in f.readlines():
        line = line.replace("\n", "")
        if 'goal' in line:
            words = re.split(",*\s|\(\*|\*\)", line)
            start_state = words[words.index('goal') + 1]
            start_state = re.split("[_=]", start_state)
            start_state = tuple(start_state)
        else:
            words = re.split("\s*and\s*|,\s*|\s+", line)
            if len(words) <= 1:
                continue
            elif (len(words) > 3) and (not read_proc):
                read_proc = 1
            if not read_proc:
                process.append(words[0])
                actions[(words[0], '0')] = []
                actions[(words[0], '1')] = []
                actions_by_hitter[(words[0], '0')] = []
                actions_by_hitter[(words[0], '1')] = []
                initial_state[words[0]] = '0'
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
                        actions_by_hitter[i].append(act)
                else:
                    for i in words[1:]:
                        temp = re.split("=", i)
                        initial_state[temp[0]] = temp[1]
    return process, actions, actions_by_hitter, initial_state, start_state
