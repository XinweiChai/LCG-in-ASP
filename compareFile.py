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
        print('true')


def batch_compare(fn1, fn2, suffix, num):
    for i in range(num):
        file_name1 = fn1 + str(i) + suffix
        file_name2 = fn2 + str(i) + suffix
        if not compare_file(file_name1, file_name2):
            return False
    return True


def count_inconclusive(fn, suffix, num):
    count = 0
    for i in range(num):
        file_name = fn + str(i) + suffix
        f = open(file_name, 'r')
        x = f.readline()
        while x:
            if 'Inconclusive' in x:
                count = count + 1
            x = f.readline()
    return count
