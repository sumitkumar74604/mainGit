'''
Wap that accept a three digit number from user and 
check whether armstrong  number or not
'''


print("\nWap that accept a three digit number from user and check whether armstrong  number or not\n")

# 153 = 1+125+27

num=int(input("Enter Number - \t"))
temp=num
count=0
while temp!=0:
    count+=1
    temp=temp//10
sum=0
temp=num
power=1
while num!=0:
    remain=num%10
    for i in range (1,count+1):
        power=power*remain
        print(i,"power - ",power)
    sum=sum+power
    power=1
    num=num//10
if temp==sum:
    print(" Given number is Armstrong  = \t\t",sum)
else:
    print("Given number isn't Armstrong ",sum)
    