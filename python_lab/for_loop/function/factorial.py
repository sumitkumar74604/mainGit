'''
3. create a function to calculate and
return factorial of a number passed in
argument
'''
print("3. create a function to calculate and return factorial of a number passed in argument")
def fact (n):
    f=1
    while n!=0:
        f=f*n
        print("f - ",f)
        n-=1
    return f

n=int(input("enter last Number :- "))
print("factorial - ",fact(n))