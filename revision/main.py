from compare import *
from parser import *
import os

input_fn = 'output1'
output_fn = 'test'

# for i in compare_file('result', 'result2', '\s'):  # reachability
#     print(i)
# print()
# for i in compare_file('result2', 'result', '\s'):
#     print(i)
# print()
# for i in compare_file('output', 'output1', '\n'):  # state transitions
#     print(i)
# print()
# for i in compare(rule_parser("rules"), rule_parser("rules2")):
#     print(i)
# print()
# for i in compare(rule_parser("rules2"), rule_parser("rules")):
#     print(i)
x = transition_parser("output")
y = rule_parser("rules")
# reachability_parser("result")

model = os.system('./AS_LF1T.exe -i ' + input_fn + ' > ' + output_fn)
