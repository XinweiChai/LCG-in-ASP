import re


def compare(x, y):
    unique = []
    for i in x:
        flag = True
        for j in y:
            if i == j:
                flag = False
                continue
        if flag:
            unique.append(i)
    return unique


def compare_file(fn1, fn2, separator):
    f1 = open(fn1, 'r')
    f2 = open(fn2, 'r')
    words1 = re.split(separator, f1.read())
    words2 = re.split(separator, f2.read())
    unique = compare(words1, words2)
    f1.close()
    f2.close()
    return unique
