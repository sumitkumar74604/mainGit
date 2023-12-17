'''
     12345
     1234
     123
     12
     1
'''
n=int(input("enter last digit - "))
for i in range (n+1,1,-1):
    for j in range (1,i):
        print(j,end="")
    print()
