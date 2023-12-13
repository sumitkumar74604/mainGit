#Q.3 Write a program to calculate sum of squares of n natural number.
print("\nQ.3 Write a program to calculate sum of squares of n natural number.\n")
n=int(input("enter your square no -  "))
a=1
sum=0
while a<=n:
    sq=a*a;
    sum=sum+sq
    print("digit - ",a,"square - ",sq,"sum - ",sum)
    a+=1
print("Sum Total = ",sum)