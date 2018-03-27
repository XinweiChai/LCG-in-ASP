import re

def readBAN(path):
    readProc = 0
    hasStartNode = 0
    process = []
    dictionary = []
    actions = {}
    actionsByHitter = {}
    initialState = []
    startState=[]
    f = open('data/'+path,'r')
    for line in f.readlines():
        line=line.replace("\n","")
        if 'goal' in line:
            hasStartNode = 1
            words = re.split(",*\s|\(\*|\*\)",line)
            startState=words[words.index('goal')+1]
            startState = re.split("[_=]",startState)
            startState = tuple(startState)
        else:
            words = re.split("\s*and\s*|\s+",line)
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
                if words[0] != 'initial_state':
                    act=[[]]
                    act.append(words[0])
                    act.append(words[1])
                    act.append(words[3])
                    for i in range(len(words)-5):
                        temp = re.split("=",words[i+5]) #last elements
                        act[0].append((temp[0],temp[1],))
                    act[0] = tuple(act[0])
                    act=tuple(act)
                    actions[(words[0],words[3])]=act
                    for i in act[0]:
                        actionsByHitter[i] = act
                else:
                    for i in range(1,len(words)):
                        temp = re.split("=",line)
                        initialState.append([temp])
            if not initialState:
                for i in process:
                    initialState.append((i,'0'))
    return dictionary,actions, actionsByHitter, initialState, startState 
