def readBAN(path):
    readProc = 0
    hasStartNode = 0
    process = []
    dictionary = []
    actions = {}
    initialState = []
    f = open('data/'+path,'r')
    for line in f.readlines():
        if 'goal' in line:
            hasStartNode = 1
            words = re.split(",*\s|\(\*|\*\)",line)
            startState[words.index('goal')+1]
            startState = re.split("_|='",startState)
        else 
            words = re.split(",*\s*",line)
            if len(words) <= 1:
                continue
            elif (len(words) > 2) and (not readProc):
                readProc = 1
                dictionary.append(process)
                #if hasStartNode
                   # startState = [dictionary[], ]
            if not readProc:
                process.append(words[0])
                continue
            else:
                #initialState = np.zeros(len(process))
                if words[0] != 'initial_state':
                    act=[[]]
                    act.append(words[0])
                    act.append(words[1])
                    act.append(words[3])
                    for i in range(len(words)-5):
                        temp = re.split("=",words[i+5]) #last elements
                        act[0].append([temp[0],temp[1]])
                    act[0] = tuple(act[0])
                    act=tuple(act)
                    actions[words[3]]=act
                else:
                    for i in range(1,len(words)):
                        temp = re.split("=",line)
                        initialState.append([temp])
                        #initialState[process.index(temp[0])] = temp[1]
    return dictionary,actions,initialState,startState 
