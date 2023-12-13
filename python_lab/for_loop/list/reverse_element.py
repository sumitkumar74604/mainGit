'''
reverse element :-
'''

print("enter last digit - ",end="")
num=int(input())
a1=[]
a4=[]

for i in range (num):
    print("element - ",end="")
    a=int(input())
    a1.append(a)
print("inputs - ",a1)
print()
rev=0
for i in range(len(a1)):
    while a1[i]!=0:
        remain = a1[i]%10
        rev=rev*10+remain
        a1[i]=a1[i]//10
    a4.append(rev)
    #a1[i]=rev
    rev=0
#sprint("reverse elements - ",a1)
print("reverse - ",a4)
temp=[]
for i in range  (num,0):
    temp[i]=a1[i]
    num-=1
print("series reverse - ",temp)
