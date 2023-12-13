# Q.1 Write a program to print Fibonacci Series.
print("\nQ.1 Write a program to print Fibonacci Series.\n")
a=0;b=1;c=0;x=0
n=int(input("enter last digit\t"))
while a<=n:
    c=a+b
    print(a,"+",b,"=",c)
    a=b
    b=c
    a+=1