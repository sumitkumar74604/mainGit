arre=[10,20,3,0,45,8,71,34,3,45,3,100]
arre2=[]
search_num=int(input("Enter number for serching -\t"))
print("--------------------------------------------")
print(" Before Delete Index data - ",arre)
count=0
for i in range (len(arre)):
    if arre[i]!=search_num:
        arre2.append(arre[i])
print("After Delete serched Number \n")
arre=arre2
print("Avilable -  ",arre)
    
