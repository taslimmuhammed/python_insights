f = open("C:\\Users\\tasli\\Desktop\\Folders\\AI\\python insights\\text.txt","w")
f.write("i love js")
f.close()
# for appending
f = open("C:\\Users\\tasli\\Desktop\\Folders\\AI\\python insights\\text.txt","a")
f.write("\ni love java")
f.close()
# reading
f = open("C:\\Users\\tasli\\Desktop\\Folders\\AI\\python insights\\text.txt","r")
for line in f:
    tokens = line.split(' ')
    print(tokens)

# r+ for both read ans write
# w+ both read and write, create file if not exist
with open("C:\\Users\\tasli\\Desktop\\Folders\\AI\\python insights\\text.txt","w+") as f:
    print(f.read())
    # no need to close in this