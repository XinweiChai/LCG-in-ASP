def compare_file(fn1, fn2):
    f1 = open(fn1, 'r')
    f2 = open(fn2, 'r')
    x1 = f1.readline()
    x2 = f2.readline()
    equal = True
    while x1:
        if x2 == '*** Killed ***\n':
            x1 = f1.readline()
            x2 = f2.readline()
            continue
        if x1 != x2:
            equal = False
            break
        x1 = f1.readline()
        x2 = f2.readline()
    if equal:
        return True
        #print('true')
    else:
        return False

def batch_compare(fn1, fn2, suffix, num):
    for i in range(num):
        file_name1 = fn1 + str(i) + suffix
        file_name2 = fn2 + str(i) + suffix
        if not compare_file(file_name1, file_name2):
            return False
    return True


def count_result(fn, suffix, num):
    inconc = 0
    trues= 0
    falses= 0
    for i in range(num):
        file_name = fn + str(i) + suffix
        f = open(file_name, 'r')
        x = f.readline()
        while x:
            if 'Inconclusive' in x or 'Inconc' in x or 'Killed' in x:
                inconc = inconc + 1
            if 'True' in x:
                trues = trues + 1
            if 'False' in x:
                falses = falses + 1
            x = f.readline()
    return trues, falses, inconc
