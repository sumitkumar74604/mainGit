'''
Wap to calculate Smallest number out of given three Number
'''
print("\nWap to calculate Smallest number out of given three Number\n")

num=int(input("Enter Number - \t"))
temp=num
while num!=0:
    remain=num%10
    if temp>=remain:
        temp=remain
    num=num//10
print("Smallest Number - \t",temp)
