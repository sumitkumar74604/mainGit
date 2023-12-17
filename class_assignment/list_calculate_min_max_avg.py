'''
Wap to take Number from user and store in list calculate the sum 
Max,Min,Avg;

'''
print("\nWap to take Number from user and store in list calculate the sum Max,Min,Avg;\n")
sum=0
max=0
min=10
arre=[]
#-----------
num=int(input("Enter last digit to follow aree - \t"))
for i in range(num+1):
    print([i],"Enter List Number -\t",end="")
    digit=int(input())
    arre.append(digit)
#arre=[10,85,30,40,500,60,70]
print("----------------------------------------------")
for i in range(len(arre)):
    sum=sum+arre[i]
    if max<=arre[i]:
        max=arre[i]
    if min>=arre[i]:
        min=arre[i]
avg=sum/len(arre)
print("Sum - ",sum)
print("Avg - ",avg)
print("Max - ",max)
print("Min - ",min)