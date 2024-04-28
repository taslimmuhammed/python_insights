import time
import multiprocessing

sqr_res = []
def calc_sqr(numbers):
    for num in numbers:
        sqr_res.append(num**2)
    print("square from new process ", sqr_res)

def calc_cube(numbers,res):
    for idx,num in enumerate(numbers):
        res[idx] = num**3

if __name__ == "__main__":
    array = [3,5,7,6,8,9]
    t = time.time()
    p1 = multiprocessing.Process(target=calc_sqr, args=(array,))
    cube_res = multiprocessing.Array('i',6) # i means integer, d means double
    val = multiprocessing.Value('d',0.0) # create a shared memory double variable
    # multiprocessing queue is also available
    p2 = multiprocessing.Process(target=calc_cube, args=(array,cube_res))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(" cube using shared memory = ",cube_res[:])
