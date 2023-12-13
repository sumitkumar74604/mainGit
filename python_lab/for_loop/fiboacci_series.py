'''
write a program to print fiboacci series
'''
n=int(input("enter last digit - "))
a=0
b=1
c=0
for i in range(1,n):
    c=a+b
    print(a,"+",b," - ",c)
    a=b
    b=c