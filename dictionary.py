d = {
    "tom":7594943308,
    "rob":6214258937,
    "joe":1234567890
}
print(d["tom"])
del d["rob"]
for key in d:
    print(key,d[key])