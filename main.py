from batch_test import *
from generate_model import *
from timeit import default_timer

"""
sizes1 = list(range(10, 100, 10))
sizes2 = list(range(100, 100, 1001))
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
"""
size = 4
density = 3
num_tran = size * density
if __name__ == '__main__':
    write_file(generate_random_an(size, num_tran), "//revision//model", size)
