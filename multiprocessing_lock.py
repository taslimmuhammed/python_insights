import time
import multiprocessing

def fxn(number,lock):
    lock.acquire()
    number.value = number.value - 200
    lock.release()

if __name__ == "__main__":
    val = multiprocessing.Value('i',0) 
    lock = multiprocessing.Lock()
    p = multiprocessing.Process(target=fxn, args=(val,lock))
    p.start()
    p.join()
    print(val.value)
