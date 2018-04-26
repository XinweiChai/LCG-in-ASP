f1 = open('data_egfr_out_compare', 'r')
f2 = open('run-egfr104.out_compare', 'r')
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
