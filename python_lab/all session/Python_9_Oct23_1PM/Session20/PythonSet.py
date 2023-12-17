'''
Set:
It is one of 4 Built-in data types in python.
It is a squence used to store multiple data in a single variable.
unordered
unchangable
unindexed
not allow duplicate value
'''

set1 = {"g","o","o","g","l","e"}
print(set1)
print("Type is:",type(set1))
print("Length is:",len(set1))
#======
for x in set1:
    print(x)
print("==================")

set1.add("a")
print(set1)
print("Length is:",len(set1))
print("==========")
set2 = {"r","a","h","u","l"}
set1.update(set2)
print(set1)
print("-------")
set1.remove("r")
print(set1)
print("------")
set1.clear()
print(set1)

