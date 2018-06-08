from test import *
import multiprocessing


def foo1(return_dict, n):
    return_dict[0] = foo(n)


#if __name__ == '__main__':
def foo2():
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    p = multiprocessing.Process(target=foo1, args=(return_dict, 1))
    p.start()
    p.join(3)
    if p.is_alive():
        p.terminate()
        return 0
    p.join()
    return return_dict[0]
    # p = multiprocessing.Process(target=foo, name="Foo", args=(10,))
    # p.start()
    ## Wait 10 seconds for foo
    ##time.sleep(3)
    # p.join(10)
    ## Terminate foo
    # if p.is_alive():
    #    p.terminate()
    ## Cleanup
    #    #return "timeout"
    #    #p.join()
    #    p.join
    # return p
