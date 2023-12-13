'''
Wap that accept four digit number from user and calculate the sum of first and last number
'''


print("\nWap that accept four digit number from user and calculate the sum of first and last number\n")

num=int(input("Enter your Digit - \t"))
sum=0
while num!=0:
    remain=num%10
    sum=sum+remain
    num=num//10
print("Sum of Given Digit - ",sum)