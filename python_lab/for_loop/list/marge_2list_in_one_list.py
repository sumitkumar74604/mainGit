'''
marge 2 list in 1 list
a1=1,2,3,4,5;
b1 =6,7,8,9,10
c1 = 1,2,3,4,5,6,7,8,9,10
'''
#print("enter your last elements - ",end="")
#num=int(input())
a1=[]
b1=[]
c1=[]
d1=[]
print("enter last digit for 1st list  - ",end="")
num=int(input())
print("1st list - ")
for i in range  (num):
    print(i," elements - ",end="")
    x=int(input("a1- "))
    a1.append(x)

print("enter last digit for 2nd list  - ",end="")
num1=int(input())
print("2st list - ")
for i in range  (num1):
    print(i," elements - ",end="")
    x=int(input("b1- "))
    b1.append(x)
n=(len(a1+b1))
#--------------------------
print("marge without append function")
k=0
for i in range(n):
    if i<num:
        c1=a1[i]
    else:
        c1=b1[k]
        k+=1
    print(" ",c1,"  ",end="")
print()
#---------------------------------
print("marge with append function ")
for i in range (len(a1)):
    d1.append(a1[i])
for i in range (len(b1)):
    d1.append(b1[i])
#-----------------------------
print("a1 -",a1,end="")
print()
print("b1 -",b1,end="")
print()
print("with append function - ",d1,end="")
print()