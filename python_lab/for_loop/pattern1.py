'''
     5
    45
   345
  2345
 12345    
'''
n=int(input("enter last digit"))
for i in range(n,0,-1):
    for k in range(i,1,-1):
        print("-",end="")
    for j in range(i,n+1):
        print(j,end="")
    print()
