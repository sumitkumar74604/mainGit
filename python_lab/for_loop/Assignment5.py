'''#Reverse element 
listitem = [10,20,30,40,50]
listitem = [50,40,30,20,10]
#----
#merge two list in third list
l1 = [1,2,3,4,5]
l2 = [6,7,8,9,10]
'''

data=[10,20,30,40,50]
print("List is :",data)
data1=[]
n=len(data)
for x in range(n):
    data1.insert(0,data[x])
print("The reverse of the list is ",data1)

l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
for x in range(len(l2)):
    l1.append(l2[x])
print("The merged list is:",l1)