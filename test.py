import time


# Your foo function
def foo(n):
    for i in range(10000 * n):
        print("Tick")
        time.sleep(1)
    return 1
