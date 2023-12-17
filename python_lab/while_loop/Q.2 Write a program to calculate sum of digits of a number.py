#Q.2 Write a program to calculate sum of digits of a number.

#input from user
num =int(input("Enter number"))
Sum=0
rem=0
while num!=0:
    rem = num%10
    Sum +=rem
    num=num//10

print(Sum) 