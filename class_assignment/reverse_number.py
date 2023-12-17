'''
Wap that accept a three digit number from user  and obtain
reverse of the number
'''

print("\nWap that accept a three digit number from user  and obtain reverse of the number\n")

num=int(input("Enter Three combination Digit \t"))
while num>999 or num<100:
    num=int(input("Enter Three combination Digit \t"))
    
rev=0
sum=0
while num!=0:
    remain=num%10
    rev=rev*10+remain
    sum+=remain
    num=num//10
print("Reverse Number of "," is - ",rev)
print("Sum of Reverse num is - ",sum)
