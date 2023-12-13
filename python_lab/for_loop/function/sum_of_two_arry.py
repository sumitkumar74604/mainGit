
'''
5. Create a function that accept two Int
arrays and return sum of all elements of
both arrays
'''
print("5. Create a function that accept two Int arrays and return sum of all elements of both arrays")
print("------------- Without Function -------------- ")
a=[11,22,33,44,55]
b=[11,22,33,44,55]
sum=0
print("[I] [A] [b] [Sum]")
for i in range (len(b)):
    sum=sum+a[i]+b[i]
    print([i],a[i],"+",b[i],"-",sum)
    sum=0
print("*************************************")
print("----- With Function ------")
def array(a=[],b=[]):
    sum = 0
    print("[I] [A] [b] [Sum]")
    for i in range (5):
        sum=sum+a[i]+b[i]
        print([i],a[i],"+",b[i],"-",sum)
        sum=0
array(a=[11,22,33,44,55],b=[11,22,33,44,55])
print("*************************************")
print("----- With Function user input ------")
def array(a=[],b=[]):
    sum = 0
    print("[I] [A] [b] [Sum]")
    for i in range (len(b)):
        sum=sum+a[i]+b[i]
        print([i],a[i],"+",b[i],"-",sum)
        sum=0
a=[]
b=[]
print("enter last digit of A :-",end="")
num=int(input())
for i in range (num):
    print([i],"enter element :-",end="")
    x=int(input())
    a.append(x)
print("enter last digit of B :-",end="")
num1=int(input())
for i in range (num):
    print([i],"enter element :-",end="")
    x=int(input())
    b.append(x)
print("---------------------------------")
array(a,b)
print("*********************************s")