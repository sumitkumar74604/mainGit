'''
Wap to prefect no.
'''
sum=0
num=int(input("enter your end digit"))
for i in range(1,num):
    if num%i==0:
        sum=sum+i
    if i==num:
        print("prefect")
    else:
        print("not")