#Q.7 Write a program that accepts a number from user and check given number is prime number or not.

#getting value form user
num =int(input("Enter number"))
Sum=0
i=1

#find sum of squares of n natural number.
while i<=num:
    if num%i==0:
        Sum+=1
    i+=1
if Sum==2:
    print("Prime number")
else:
    print("Other number")

