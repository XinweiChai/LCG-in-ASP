import re
from m2rit.parser import rule_parser


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
    with open(fn1, 'r') as f1:
        with open(fn1, 'r') as f2:
            words1 = re.split(separator, f1.read())
            words2 = re.split(separator, f2.read())
            unique = compare(words1, words2)
    return unique


if __name__ == "__main__":
    for i in compare_file('result', 'result2', '\s'):  # reachability
        print(i)
    print()
    for i in compare_file('result2', 'result', '\s'):
        print(i)
    print()
    for i in compare_file('output', 'output1', '\n'):  # state transitions
        print(i)
    print()
    for i in compare(rule_parser("rules"), rule_parser("rules2")):
        print(i)
    print()
    for i in compare(rule_parser("rules2"), rule_parser("rules")):
        print(i)
