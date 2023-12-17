'''
6. Create a function that accepts two
tuples of type (Float,Int) and return
t1.0/t2.0 + t1.1*t2.1 
'''

print("6. Create a function that accepts two tuples of type (Float,Int) and return t1.0/t2.0 + t1.1*t2.1 ")
t1 = (10.11,11.22,33.11,44.22,55.88)
t2 = (9,8,7,6,5)
sum=0
m=1
print("[i]  [A]   [B]     [A]   [B]  - [sum]")
for i in range (len(t1)):
    #sum=sum+t1[i]+t2[i]
    #sum=sum+((t1[i]/t2[i])+(t1[i]*t2[i]))  
    sum=((t1[i]/t2[i])+(t1[i]*t2[i]))
    print([i],t1[i],"/",t2[i]," + ",t1[i],"*",t2[i]," - ",sum)
print("-------------------------------------------------------")
print("-------------- With aprgument function ----------")
sum=0
def tup(t1=(),t2=()):
    for i in range (len(t1)):
        sum=((t1[i]/t2[i])+(t1[i]*t2[i]))  
        return sum

t1 = (10.11,11.22,33.11,44.22,55.88)
t2 = (9,8,7,6,5)
z=tup(t1,t2)
print([i],t1[i],"/",t2[i]," + ",t1[i],"*",t2[i]," - ",z)