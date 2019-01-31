from batch_test import *
from generate_model import *
from timeit import default_timer
from reach import *


sizes1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sizes2 = [200, 300, 400, 500, 600, 700, 800, 900, 1000]
sizes = sizes1 + sizes2
size_density = 3
times = [1, 2, 3, 4, 5, 6, 7]
num_tran_var = size_density * times
models = 10
iteration = 50
automata = 20

time_recorder = {}
if __name__ == '__main__':
    f = open("data//runtime", 'w')
    for i in sizes:
        print(i)
        num_tran = size_density * i
        generate_files(models, i, num_tran)
        start = default_timer()
        for j in range(models):
            batch("data//inputFile", "data//model_" + str(i) + "//model_" + str(j))
        stop = default_timer()
        time_recorder[i] = (stop - start) / models / 20
        f.write(str(i) + ":" + str(time_recorder[i]) + '\n')
asp_exhaust_solve("tcr.lp")
asp_exhaust_solve("th.lp")
asp_exhaust_solve("test.lp")
