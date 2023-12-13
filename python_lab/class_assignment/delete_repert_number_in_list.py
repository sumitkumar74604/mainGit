''''
Wap to search a number and delete all(if repeat) in List.
'''

print("\nWap to search a number and delete all(if repeat) in List.\n")
arre=[]
digit=int(input("Enter last Digit to follow List :-"))
for i in range (digit):
    print([i]," Enter number of list - \t",end="")
    series=int(input())
    arre.append(series)
search_num=int(input("Enter number for serching -\t"))
print("--------------------------------------------")
print(" Before Delete Index data - ",arre)
count=0
for j in range (len(arre)):
    for i in range (len(arre)):
        if arre[i]==search_num:
            print(" Founded Number ",[i],arre[i])
            del arre[i]
            break
print("\n-------------------------------------\n")
print("After Delete serched Number \n")
print("Avilable -  ",arre,"\n")
    
    
            
        
        
