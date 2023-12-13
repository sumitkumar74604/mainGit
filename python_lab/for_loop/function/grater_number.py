'''
1. create a function to print greater of two numbers passed in argument
'''

print("1. create a function to print greater of two numbers passed in argument")
def grater (x,y):
    if x>y:
        print("grater A :- ",end="")
        z=x
    else:
        print("grater B :- ",end="")
        z=y
    return z

x=int(input("enter A :- "))
y=int(input("enter B :- "))
print(grater(x,y))
print("--------------------------")
print("-------------- Print with Max function --------------")
print("Grater - :- ",max(x,y))