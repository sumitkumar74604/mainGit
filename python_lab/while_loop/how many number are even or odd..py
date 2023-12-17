#Q.4 Write a program to accept n number from user and show how many number are even or odd.

#getting value form user
num =int(input("Enter number"))
ESum=0
OSum=0
i=1

#how many number are even or odd.
while i<=num:
    if i%2==0:
        ESum+=1
        print("Even",i," ")
    else:
        OSum+=1
        print("Odd",i," ")
    i+=1

print("Count of Even:",ESum)
print("Count of Odd:",OSum)