'''
Resursion Function: Function calling itself.
5! = 5x4x3x2x1
'''
def printNumber(n):
    if n!=0:
       print("Number is:",n)
       printNumber(n-1)
print("-----------")
#func calling
printNumber(5)


a=1
def printNumber1(a,n):
    if a<=n:
       print("Number is:",a)
       printNumber1(a+1,n)
print("-----------")

#func calling
printNumber1(1,15)



def factorial(n):
    total = 0
    if n==1:
       return 1
    else:
        total = n*factorial(n-1)
        print(total)
        return total
#---

print("Factorial is :",factorial(5))     