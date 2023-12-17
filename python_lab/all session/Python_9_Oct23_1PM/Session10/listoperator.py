'''
Operators used in list
'''
# + concatenation
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
l3 = []
l=l1+l2
print(l)
print("-----------------")
for data in l1:
    l3.append(data)
for data in l2:
    l3.append(data)
print(l3)    
print("-----------------")
#* multiplier
l1 = [1,2,3,4]
l = l1*3
print(l)
print("-----------------")

#membership operator in , not in
cricketplayer = ["Kapil Dev","Sachin Tendulkar","Virendra Shewag","M.S Dhoni","Virat Kohli"]

p = "Virendra Shewag"
r = p in cricketplayer
print(r)
r = p not in cricketplayer
print(r)

#slice operator
l1 = [10,20,30,40,50,60,70,80,90,100]
print("Range:",l1[:])
print("Range from 2:",l1[2:])
print("Range from 2:6",l1[2:6])
print("Range from 1:8:2",l1[1:8:2])
print("Range from :6",l1[:6])
print("Range from -6:-2",l1[-6:-2])
print("Range from -6:",l1[-6:])
print("Range from -6:-2:-2",l1[-6:-2:2])

#convert string into list
name = "rahul sharma neha sharma"
newl = list(name)
print(newl)

l = name.split(" ")
print(l)