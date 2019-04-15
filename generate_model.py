import random
import os


def generate_random_an(an_size, an_num_tran):
    if an_num_tran > an_size * an_size:
        an_num_tran = an_size * an_size
    transition_set = []
    for i in range(an_num_tran):
        head = random.randint(1, an_size)
        temp = list(range(1, an_size + 1))
        sign = random.choice([1, -1])
        temp.remove(head)
        head = head * sign
        body = []
        next_tr = 1  # at lease one variable in the body
        while next_tr > 0.2 and temp:
            next_tr = random.random()
            sign = random.choice([1, -1])
            dice = random.choice(temp)
            body.append(sign * dice)
            temp.remove(dice)
        trans = [head, body]
        mark = False
        for j in transition_set:
            if head == j[0] and set(body) > set(j[1]):
                mark = True
                break
        if mark:
            continue
        if [-head, body] not in transition_set:
            transition_set.append(trans)
    return transition_set


# def generateRandomTransition(size,numTran):

def write_file(model, fn, an_size):
    f = open(fn, 'w')
    for i in range(an_size):
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


def generate_files(amount, an_size, an_num_tran):
    path = 'data//model_' + str(an_size)
    if not os.path.exists(path):
        os.makedirs(path)
    for i in range(amount):
        write_file(generate_random_an(an_size, an_num_tran), path + "//model_" + str(i), an_size)


if __name__ == "__main__":
    size = 20
    num_tran = 60
    models = 10

    x = generate_random_an(size, num_tran)
    write_file(x, 'testmodel', size)
    generate_files(models, size, num_tran)
