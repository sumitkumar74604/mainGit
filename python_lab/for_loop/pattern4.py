'''
54321           54321
4321             4321
321               321
21                 21
1                   1
'''
n=int(input("enter last digit - "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()


print("\n")

for i in range(n,0,-1):
    for k in range(0,n-i):
        print("-",end="")
    for j in range(i,0,-1):
        print(j,end="")
    print()