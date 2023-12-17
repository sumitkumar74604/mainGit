
a1 = [4,10,78,35,15,50]
a2 = [65,89,1,64,75,20]
print("entered element ",a1)
print("entered element ",a2)
a3 = a1+a2
print("marge element - ")
print(a3)

#------------
# shorting element:-
for x in range(len(a3)):
    for y in range(x+1,len(a3)):
        if a3[x]>=a3[y]:
            temp=a3[x]
            a3[x]=a3[y]
            a3[y]=temp
print("shorting Accsending order----------")
print(a3)


#=-----------------------
# reverse array elements :-
rev=0
for x in range(len(a3)):
    while a3[x]!=0:
        remain=a3[x]%10
        rev=rev*10+remain
        a3[x]=a3[x]//10
    a3[x]=rev
    rev=0
print(a3,end="")
    