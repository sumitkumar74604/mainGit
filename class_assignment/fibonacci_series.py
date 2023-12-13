''''
Wap to print Fibonacci Series :-
'''

print("\nWap to print Fibonacci Series :-\n")
last_digit=int(input("Enter Last digit :- \t"))
a,b=0,1;
print("\t i   a  +  b  -  c\n")
while last_digit!=0:
    c=a+b
    print("\t",last_digit," ",a," + ",b," - ",c)
    a=b;
    b=c;
    last_digit-=1