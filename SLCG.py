def SLCG(path):
    readProc = 0
    hasStartNode = 0
    process = []
    dictionary = []
    actions = []
    f = open('data/'+path,'r')
    for line in f.readlines():
        if 'goal' in line
            hasStartNode = 1
            words = re.split(",*\s|\(\*|\*\)",line)
            startState[words.index('goal')+1]
            startState = re.split("_|='",startState)
        else 
            words = re.split("\s*",line)
            if len(words) <= 1
                continue
            elif (len(words) > 2) and (not readProc)
                readProc = 1
                dictionary.append(process)
                #if hasStartNode
                   # startState = [dictionary[], ]
            if not readProc
                process.append(words[0])
                continue
            else
                initialState = np.zeros(len(process))
                if not words[0] == 'initial_state'
                    act = []
                else
                    for i in range(4)
                        temp = re.split(",*\s",line)
                        initialState 
    return dictionary,actions,initialState,startState 
                
