#Q.5 Write a program to find LCM of two numbers.
print("\nQ.5 Write a program to find LCM of two numbers.\n")
x=int(input(" enter 1st digit - "))
y=int(input(" enter 1st digit - "))
if x > y:
    z = x
else:
    z = y
while(1):
    if((z % x == 0) and (z % y == 0)):
        print( "if",x,y,z)
        lcm = z
        print( "loop",lcm)
        break
    z += 1
        
print(lcm)

    

