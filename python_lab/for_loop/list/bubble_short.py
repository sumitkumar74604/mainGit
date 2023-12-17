'''
shorting Ascending descending with user input
'''

print("enter last digit - ",end="")
num=int(input())
a1=[]
a2=[]
for i in range(num):
    print(i," element - ",end="")
    a=int(input())
    a1.append(a)
#--------------------------#
a2=a1
print("------------- inputs ---------- ")
print("inputs - ",a1,end="")
for i in range(len(a1)):
    for j in range(i,len(a1)):
        if a1[i]>a1[j]:
            temp=a1[i]
            a1[i]=a1[j]
            a1[j]=temp
        if a2[i]<a2[j]:
            temp=a2[i]
            a2[i]=a2[j]
            a2[j]=temp
print("\n --------------------- -------\n")
print("Ascending order",a1)
print()
print("\n --------------------- -------\n")
print("Dscending order",a2)
print()