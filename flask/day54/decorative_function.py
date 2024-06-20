import time

def speed_clac_decorator(func):
    start = time.time()
    func()
    finish = time.time()

    print(func.__name__,round(finish - start, 2))

@speed_clac_decorator
def slow_func():
    for i in range(10000000):
        i+1
    
@speed_clac_decorator
def fast_func():
    for i in range(1000000):
        i*i
    

