def generate(initState,  lcgEdges):
    f = open("fact.lp",'w')
    for i in initState.items():
        f.writelines("init(\""+i[0]+"\","+i[1]+").\n")
    node=[]
    for i in enumerate(lcgEdges):
        if len(i[1])==2:
            node.append((i[1],i[0]))
            f.writelines("node(\"" + i[1][0] + "\"," + i[1][1]+ ","+ str(i[0]) + ").\n")
    node=dict(node)
    for i in node:
        if i not in initState.items():
            for j in lcgEdges[i][0][0]:
                f.writelines("parent("+str(node[i])+","+str(node[j])+").\n")
    f.close()
