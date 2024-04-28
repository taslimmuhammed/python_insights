import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end  = time.time()
        print(func.__name__+" took "+str(end-start)+" sec")
        return result
    return  wrapper

@time_it
def calc_sqr(numbers):
    result = []
    for number in numbers:
        result.append(number**2)
    return result
@time_it
def calc_cube(numbers):
    result = []
    for number in  numbers:
        result.append(number**3)
    return result

array = range(1,100000000)
calc_cube(array)
calc_sqr(array)