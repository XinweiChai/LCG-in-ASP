import random
import os


def generate_random_AN(size, num_tran):
    if num_tran > size * size:
        num_tran = size * size
    transition_set = []
    for i in range(num_tran):
        head = random.randint(1, size)
        temp = list(range(1, size + 1))
        sign = random.choice([1, -1])
        temp.remove(head)
        head = head * sign
        sign = random.choice([1, -1])
        dice = random.choice(temp)
        body = [sign * dice]
        temp.remove(dice)
        nextTr = random.randint(0, 10)
        while nextTr > 1 and temp:
            nextTr = random.randint(0, 10)
            sign = random.choice([1, -1])
            dice = random.choice(temp)
            body.append(sign * dice)
            temp.remove(dice)
        trans = [head, body]
        mark = False
        for i in transition_set:
            if head == i[0] and set(body) > set(i[1]):
                mark = True
                break
        if mark:
            continue
        if [-head, body] not in transition_set:
            transition_set.append(trans)
    return transition_set


# def generateRandomTransition(size,numTran):

def writeFile(model, fn, size):
    f = open('model_' + str(size) + '//' + fn, 'w')
    for i in range(size):
        f.writelines('n' + str(i + 1) + ' [0, 1]\n')
    f.writelines('\n')
    for i in model:
        f.writelines('n' + str(abs(i[0])))
        if i[0] > 0:
            f.writelines(' 0 -> 1 when ')
        else:
            f.writelines(' 1 -> 0 when ')
        for j in i[1][0:-1]:
            f.writelines('n' + str(abs(j)) + '=')
            if j < 0:
                f.writelines('0')
            else:
                f.writelines('1')
            f.writelines(' and ')
        f.writelines('n' + str(abs(i[1][-1])) + '=')
        if i[1][-1] < 0:
            f.writelines('0')
        else:
            f.writelines('1')
        f.writelines('\n')
        # for j in i[1]:
        #    f.writelines('n'+str(i[0])+' 1 -> 0 when ')
        #    f.writelines('n'+str(abs(j))+'=')
        #    if j>0:
        #        f.writelines('0')
        #    else:
        #        f.writelines('1')
        #    f.writelines('\n')


def generateFiles(amount, size, num_tran):
    if not os.path.exists('model_' + str(size)):
        os.makedirs('model_' + str(size))
    for i in range(amount):
        writeFile(generate_random_AN(size, num_tran), 'model' + str(i), size)
