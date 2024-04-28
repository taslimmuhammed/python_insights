items = ["bread","pasta","fruits","veggies"]
itr = iter(items)
print(next(itr))
rev = reversed(items)
for i in rev:
    print(i)

# generator
def channels_next():
    yield "CNN"
    # the next fxn stops here and next time start right after previuos yield
    yield "ESPN"

itr = channels_next()
print(next(itr))
print(next(itr))
# for loop also works on it same as array 

def fib():
    a,b=0,1
    while True:
        yield a
        a,b = b,a+b
f = fib()
print(next(f))
print(next(f))
# infinite sequence of numbers using generators
for f in fib():
    if(f>100):
        break
    print(f)