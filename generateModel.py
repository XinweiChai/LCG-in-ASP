import random
def generateRandomBN(size,numTran):
    if numTran > size*size:
        numTran = size*size
    transitionSet=[]
    for i in range(numTran):
        head=random.randint(1,size)
        temp = list(range(1,size+1))
        temp.remove(head)
        sign=random.choice([1,-1])
        dice=random.choice(temp)
        body=[sign*dice]
        temp.remove(dice)
        nextTr=random.randint(0,10)
        while nextTr>5 and temp:
            nextTr=random.randint(0,10)
            sign=random.choice([1,-1])
            dice=random.choice(temp)
            body.append(sign*dice)
            temp.remove(dice)
        trans=[head,body]
        if trans not in transitionSet:
            transitionSet.append(trans)
    return transitionSet

#def generateRandomTransition(size,numTran):

def writeFile(model,size):
    f=open('randomGenerateBN','w')
    for i in range(size):
        f.writelines('n'+str(i)+' [0, 1]\n')
    f.writelines('\n')
    for i in model:
        f.writelines('n'+str(i[0])+' 0 -> 1 when ')
        for j in i[1][0:-1]:
            f.writelines('n'+str(abs(j))+'=')
            if j<0:
                f.writelines('0')
            else:
                f.writelines('1')
            f.writelines(' and ')
        f.writelines('n'+str(abs(i[1][-1]))+'=')
        if i[1][-1]<0:
            f.writelines('0')
        else:
            f.writelines('1')
        f.writelines('\n')
        for j in i[1]:
            f.writelines('n'+str(i[0])+' 1 -> 0 when ')
            f.writelines('n'+str(abs(j))+'=')
            if j>0:
                f.writelines('0')
            else:
                f.writelines('1')
            f.writelines('\n')
