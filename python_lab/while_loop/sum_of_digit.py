#Q.2 Write a program to calculate sum of digits of a number.
print("\nQ.2 Write a program to calculate sum of digits of a number.\n")
n=int(input("enter number \t"))
sum=0
while n!=0:
    remain=n%10;
    sum=sum+remain
    n=n//10

print("sum of given number = ",sum)