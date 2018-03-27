def generate(initState, lcgNodes, lcgEdges):
    f = open("fact.lp",'w')
    for i in initState:
        f.writelines("init("+i[0]+","+i[1]+").\n")
    num=list(enumerate(lcgEdges))
    node=[]
    for i in enumerate(lcgEdges):
        if len(i[1])==2:
            node.append((i[1],i[0]))
            f.writelines("node(" + ",".join(i[1]) + "," + str(i[0]) + ").\n")
    node=dict(node)
    for i in node:
        if i not in initState:
            temp=lcgEdges[i]
            for j in temp:
                for k in lcgEdges[j]:
                    f.writelines("parent("+str(node[i])+","+str(node[k])+").\n")#+","+k+"\n")
    f.close()
