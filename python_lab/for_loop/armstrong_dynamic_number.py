'''
wap to print armstrong no.
'''
print(" Wap to print armstrong no.")
num=int(input("enter digit "))
a=1
n=a
while a<=num:
    count=0
    for i in range(1,n):
        if n!=0:
            count+=1
            n=n//10
    #print("count - ",count)
   # print("temp ",temp)
    power=1
    temp=n
    sum=0
    while temp!=0:
        remain=temp%10
        for j in range(0,count):
            power=power*remain
       # print("power",power)
        sum=sum+power
        power=1
        temp=temp//10
    if sum==temp:
        print("a - ",sum)
    a+=1