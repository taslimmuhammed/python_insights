import time
import threading
def calc_sqr(numbers):
    result = []
    for number in numbers:
        result.append(number**2)
    time.sleep(0.2) 
    return result
def calc_cube(numbers):
    result = []
    for number in  numbers:
        result.append(number**3)
    return result
if __name__ == "__main__":
    array = range(1,1000000)
    t = time.time()
    t1 = threading.Thread(target=calc_sqr, args=(array,))
    t2 = threading.Thread(target=calc_cube, args=(array,))
    t1.start()
    t2.start()

    t1.join() # wait until the t1 is finished
    t2.join()

    print("total time = ", time.time()-t)