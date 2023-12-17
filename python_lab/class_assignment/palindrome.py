'''
Wap that accept a three digit number from user and check whether it is Palindrome or not
'''

print("\nWap that accept a three digit number from user and check whether it is Palindrome or not\n")

num=int(input("Enter Number -\t"))
temp=num
rev=0
while num!=0:
    remain=num%10
    rev=rev*10+remain
    num=num//10
if temp==rev:
    print("Number is polindrone\t",rev)
else:
    print("Number isn't polindrone\t",rev)