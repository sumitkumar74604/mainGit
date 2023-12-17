#Q.4 Write a program to accept n number from user and show how many number are even or odd.
print("\nQ.4 Write a program to accept n number from user and show how many number are even or odd.\n")
n=int(input("enter last digit - "))
a=1
ecount=0
ocount=0
while a<=n:
    if a%2==0:
        ecount+=1;
        print("eve - ",a)
    else:
        ocount+=1
        print("odd - ",a)
    a+=1
print("even total no. - ",ecount)
print("odd total no. - ",ocount)