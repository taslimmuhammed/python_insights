numbers = [0,1,2,3,4,5,6,7]
# initializing
num_set = set(numbers)
s = {2,4,4,6,2,1,423,42,56,}
s.add(10)
print("Set: ", s)
print("union",s|num_set)
print("and",s&num_set)
print("diff ",s - num_set)
print("subset ",s<num_set)
# cannot add new elements to frozen set
f_set = frozenset(numbers)