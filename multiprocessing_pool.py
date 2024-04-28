# map :- split work with multiple units/cores
# reduce :- aggregate the results from these cores to one

from multiprocessing import Pool
import time
def sqr(n):
    sum = 0
    for x in range(1000):
        sum += x*x
    return sum

if __name__=="__main__":

    t1 = time.time()
    p = Pool()
    # pass in an array it'll split the work to many cores
    # p = Pool(processes = 3) can limit the max number of process to 3
    result = p.map(sqr,range(100000)) 
    p.close()
    p.join()

    print("pool took ", (time.time()-t1))

    t2 = time.time()
    result = []
    for x in range(100000):
        result.append(sqr(x))
    print("without pool ", (time.time()-t2))