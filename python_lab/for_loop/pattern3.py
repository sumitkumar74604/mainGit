'''
1                       1
23                     2 3
345                   4 5 6
678910               5 6 7 8 
1112131415         9 10 11 12 13
'''
n=int(input("enter last digit to print pattern - "))
count=0
for i in range(1,n):    #row
    for k in range(1,n-i):  #space
        print("  ",end="")   #space print
    for j in range(0,i):    #colom
        count+=1
        print(count," ",end="") #colom print
    print()