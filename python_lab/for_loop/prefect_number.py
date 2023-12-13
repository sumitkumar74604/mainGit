'''
Wap to prefect no.
'''

x=int(input("enter end range  "))
a=1
count=0
sum=0
print("prefect no. are :- ")
for j in range(a,x):
    num=j
    for i in range(1,num):
        #print("j",j)
        if num%i==0:
            sum=sum+i
#-------- Checking
    if sum==j:
        count+=1
        print(sum)
    sum=0
print("total prefect count - ",count)