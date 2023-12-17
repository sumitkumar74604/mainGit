'''
#Reverse element 
listitem = [10,20,30,40,50]
listitem = [50,40,30,20,10]
'''
item=[10,20,30,40,50]
temp=[0]*5

for i in range(len(item)):
    temp[i]=item[len(item)-1-i]
print(temp)

'''
#merge two list in third list
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
'''
i=[1,2,3,4,5]
i2=[6,7,8,9,10]
i3=[0]*10

for x in range(5):
    i.append (i2[x])
print("merged list:",i)
