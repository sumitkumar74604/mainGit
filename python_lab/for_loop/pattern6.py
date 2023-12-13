'''
            5
           545
          54345
         5432345
        543212345
         5432345
          54345
           545
            5
'''
n=int(input("enter last digit - "))
for i in range(n,0,-1):
    for k in range(i,1,-1):
        print("-",end="")
    for j in range(n,i-1,-1):
        print(j,end="")
    for l in range(j,n):
        print(l+1,end="")
    print()

for i in range (1,n):
    for k in range(0,i):
        print("-",end="")
    for j in range(n,i,-1):
        print(j,end="")
    for l in range(j,n):
        print(l+1,end="")
    print("")