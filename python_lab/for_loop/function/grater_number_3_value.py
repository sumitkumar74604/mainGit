'''
2. Create a function to print greater of 
three numbers passed in argument
'''
print("2. Create a function to print greater of three numbers passed in argument")
def grater(a,b,c):
    if a>=b and a>=c:
        print("Grater is A :- ",end="")
        z=a
    elif b>=c:
        print("Grater is B :- ",end="")
        z=b
    else:
        print("Grater is C :- ",end="")
        z=c
    return z
a=int(input("enter A :-"))
b=int(input("enter B :-"))
c=int(input("enter C :-"))
print("-----------------------------")
print(grater(a,b,c))
print("******************************")