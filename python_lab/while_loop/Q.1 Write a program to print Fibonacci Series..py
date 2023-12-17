#Q.1 Write a program to print Fibonacci Series.

#input from user
num =int(input("Enter number of Element in series"))
a=0
b=1
i=1
print(a)
print(b)
#working on serious
while i<=num:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1 