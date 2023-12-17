'''
     1
    121
   12312
  1234123
 123451234
  1234123
   12312
    121
     1
'''
n=int(input("enter last digit - "))
for i in range(1,n+1):
    for k in range(0,n-i):
        print("-",end="")
    for j in range(1,i+1):
        print(j,end="")
    for l in range(1,i):
        print(l,end="")
    print()
#------
for i in range(1,n):
    for k in range(1,i+1):
        print("-",end="")
    for j in range(1,(n+1)-i):
        print(j,end="")
    for l in range(1,n-i):
        print(l,end="")
    print()