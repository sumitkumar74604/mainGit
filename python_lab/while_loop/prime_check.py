#Q.7 Write a program that accepts a number from user and check given number is prime number or not.
print("\nQ.7 Write a program that accepts a number from user and check given number is prime number or not.\n")
n=int(input("enter last number - "))
a=1
count=0
if n==2:
    print(n,"isn't prime") 
else:
    while a<=n:
        if n%a==0:
            count+=1
            print(count,"---")
        a+=1
    if count==2:
        print(n," is prime")
    else:
        print(n,"is't prime")    


