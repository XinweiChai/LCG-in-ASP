def SLCG(path):
    f = open('data/'+path,'r')
    for line in f.readlines():
        words = re.split(",*\s|\(\*|\*\)",line)
        startState[words.index('goal')+1]
        startState = re.split("_|='",startState)

